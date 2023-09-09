from jinja2 import Environment, PackageLoader, select_autoescape
from jinja2.loaders import FileSystemLoader


def render_html(config, template_dir_override=None) -> str:

    env = Environment(
        loader=PackageLoader('adr_viewer', 'templates') if template_dir_override is None else FileSystemLoader(template_dir_override),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('index.html')

    return template.render(config=config)