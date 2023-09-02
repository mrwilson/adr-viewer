from typing import List, Iterator, Optional, Dict

import glob
from jinja2.loaders import FileSystemLoader
import mistune
import os
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader, select_autoescape
import click
from bottle import Bottle, run


def extract_statuses_from_adr(page_object) -> Iterator[str]:
    status_section = page_object.find('h2', text='Status')

    if status_section and status_section.nextSibling:
        current_node = status_section.nextSibling

        while current_node.name != 'h2' and current_node.nextSibling:
            current_node = current_node.nextSibling

            if current_node.name == 'p':
                yield current_node.text
            elif current_node.name == 'ul':
                yield from (li.text for li in current_node.children if li.name == "li")
            else:
                continue


def parse_adr_to_config(path) -> Optional[Dict]:
    adr_as_html = mistune.markdown(open(path).read())

    soup = BeautifulSoup(adr_as_html, features='html.parser')

    statuses = list(extract_statuses_from_adr(soup))

    if any([line.startswith("Amended by") for line in statuses]):
        status = 'amended'
    elif any([line.startswith("Accepted") for line in statuses]):
        status = 'accepted'
    elif any([line.startswith("Superseded by") for line in statuses]):
        status = 'superseded'
    elif any([line.startswith("Proposed") or line.startswith("Pending") for line in statuses]):
        status = 'pending'
    else:
        status = 'unknown'

    header = soup.find('h1')

    if header:
          return {
                'status': status,
                'body': adr_as_html,
                'title': header.text
            }
    else:
        return None


def render_html(config, template_dir_override=None) -> str:

    env = Environment(
        loader=PackageLoader('adr_viewer', 'templates') if template_dir_override is None else FileSystemLoader(template_dir_override),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('index.html')

    return template.render(config=config)


def get_adr_files(path) -> List[str]:
    files = glob.glob(path)
    files.sort()
    return files


def run_server(content, port) -> None:
    print(f'Starting server at http://localhost:{port}/')
    app = Bottle()
    app.route('/', 'GET', lambda: content)
    run(app, host='localhost', port=port, quiet=True)


def generate_content(path, template_dir_override=None, title=None) -> str:

    files = get_adr_files("%s/*.md" % path)

    config = {
        'project_title': title if title else os.path.basename(os.getcwd()),
        'records': []
    }

    for index, adr_file in enumerate(files):

        adr_attributes = parse_adr_to_config(adr_file)

        if adr_attributes:
            adr_attributes['index'] = index

            config['records'].append(adr_attributes)
        else:
            print("Could not parse %s in ADR format, ignoring." % adr_file)

    return render_html(config, template_dir_override)


CONVENTIONAL_ADR_DIR = 'doc/adr/'
DEFAULT_ADR_DIR_FILE = '.adr-dir'


def resolve_adr_dir(maybe_dir=None, adr_dir_file=DEFAULT_ADR_DIR_FILE):
    """
    If passed something, blindly use it. Otherwise, resolve based on
    conventions in the ADR tooling ecosystem.
    """
    def lookup():
        adr_dir = CONVENTIONAL_ADR_DIR
        if os.path.exists(adr_dir_file):
            with open(adr_dir_file, 'r') as file:
                adr_dir = file.read().strip()
        return adr_dir

    return maybe_dir if maybe_dir else lookup()


@click.command()
@click.option('--adr-path',
              default=None,
              help=f"""
                Directory containing ADR files; pass explicitly,
                read {DEFAULT_ADR_DIR_FILE} if it exists or uses {CONVENTIONAL_ADR_DIR}
              """,
              show_default=True)
@click.option('--output',        default='index.html', help='File to write output to.',                show_default=True)
@click.option('--title',         default=None,         help='Set the project title',                   show_default=True)
@click.option('--serve',         default=False,        help='Serve content at http://localhost:8000/', is_flag=True)
@click.option('--port',          default=8000,         help='Change port for the server',              show_default=True)
@click.option('--template-dir',  default=None,         help='Template directory.',                     show_default=True)
def main(adr_path, output, title, serve, port, template_dir) -> None:
    adr_path = resolve_adr_dir(adr_path)
    content = generate_content(adr_path, template_dir, title)

    if serve:
        run_server(content, port)
    else:
        with open(output, 'w') as out:
            out.write(content)
