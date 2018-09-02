import glob
import mistune
import os
from bs4 import BeautifulSoup
from jinja2 import Environment, PackageLoader, select_autoescape


def parse_adr_to_config(path):
    adr_as_html = mistune.markdown(open(path).read())

    soup = BeautifulSoup(adr_as_html, features='html.parser')

    status = soup.find('h2', text='Status').findNext('p').text

    status = 'accepted' if status == 'Accepted' else None

    header = soup.find('h1').text

    return {
        'status': status,
        'body': adr_as_html,
        'title': header
    }


def render_html(config):

    env = Environment(
        loader=PackageLoader('adr_viewer', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('index.html')

    return template.render(config=config)


def get_adr_files():
    files = glob.glob('doc/adr/*.md')
    files.sort()
    return files


def generate_content():

    files = get_adr_files()

    config = {
        'project_title': os.path.basename(os.getcwd()),
        'records': []
    }

    for index, adr_file in enumerate(files):

        adr_attributes = parse_adr_to_config(adr_file)

        adr_attributes['index'] = index

        config['records'].append(adr_attributes)

    return render_html(config)


def main():
    print(generate_content())
