from typing import List

from click import option, command

from adr_viewer.parse import parse_adr, parse_adr_files, Adr
from adr_viewer.render import (
    generate_configuration,
    render_html,
    AdrTemplateConfig,
)
from adr_viewer.server import run_server


# fmt: off
@command()
@option('--adr-path',      default='doc/adr/',   help='Directory containing ADR files.',         show_default=True)
@option('--output',        default='index.html', help='File to write output to.',                show_default=True)
@option('--title',         default=None,         help='Set the project title',                   show_default=True)
@option('--serve',         default=False,        help='Serve content at http://localhost:8000/', is_flag=True)
@option('--port',          default=8000,         help='Change port for the server',              show_default=True)
@option('--template-dir',  default=None,         help='Template directory.',                     show_default=True)
# fmt: on
def main(adr_path, output, title, serve, port, template_dir) -> None:
    adrs: List[Adr] = parse_adr_files("%s/*.md" % adr_path)

    configuration = generate_configuration(adrs, title)

    content = render_html(configuration, template_dir)

    if serve:
        run_server(content, port)
    else:
        with open(output, "w") as out:
            out.write(content)
