import glob
from jinja2.loaders import FileSystemLoader
import mistune
import os
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader, select_autoescape
import click
from bottle import Bottle, run


def extract_statuses_from_adr(page_object):
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


def parse_adr_to_config(path):
    adr_as_html = mistune.markdown(open(path).read())

    soup = BeautifulSoup(adr_as_html, features='html.parser')

    status = list(extract_statuses_from_adr(soup))

    if any([line.startswith("Amended by") for line in status]):
        status = 'amended'
    elif any([line.startswith("Accepted") for line in status]):
        status = 'accepted'
    elif any([line.startswith("Superseded by") for line in status]):
        status = 'superseded'
    elif any([line.startswith("Pending") for line in status]):
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


def render_html(config, template_dir_override=None):

    env = Environment(
        loader=PackageLoader('adr_viewer', 'templates') if template_dir_override is None else FileSystemLoader(template_dir_override),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('index.html')

    return template.render(config=config)


def get_adr_files(path):
    files = glob.glob(path)
    files.sort()
    return files


def run_server(content, port):
    print(f'Starting server at http://localhost:{port}/')
    app = Bottle()
    app.route('/', 'GET', lambda: content)
    run(app, host='localhost', port=port, quiet=True)


def generate_content(path, template_dir_override=None, title=None):

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


@click.command()
@click.option('--adr-path',      default='doc/adr/',   help='Directory containing ADR files.',         show_default=True)
@click.option('--output',        default='index.html', help='File to write output to.',                show_default=True)
@click.option('--title',         default=None,         help='Set the project title',                   show_default=True)
@click.option('--serve',         default=False,        help='Serve content at http://localhost:8000/', is_flag=True)
@click.option('--port',          default=8000,         help='Change port for the server',              show_default=True)
@click.option('--template-dir',  default=None,         help='Template directory.',                     show_default=True)
def main(adr_path, output, title, serve, port, template_dir):
    content = generate_content(adr_path, template_dir, title)

    if serve:
        run_server(content, port)
    else:
        with open(output, 'w') as out:
            out.write(content)
