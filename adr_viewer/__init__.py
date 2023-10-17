from typing import List, Optional

from click import option, command

from adr_viewer.parse import parse_adr, parse_adr_files, Adr
from adr_viewer.render import render_html, AdrTemplateConfig, generate_content
from adr_viewer.server import run_server


CONVENTIONAL_ADR_DIR = "doc/adr/"
DEFAULT_ADR_DIR_FILE = ".adr-dir"


def resolve_adr_dir(
    maybe_dir: Optional[str] = None, adr_dir_file: str = DEFAULT_ADR_DIR_FILE
):
    """
    If passed something, blindly use it. Otherwise, resolve based on
    conventions in the ADR tooling ecosystem.
    """

    def lookup():
        adr_dir = CONVENTIONAL_ADR_DIR
        if os.path.exists(adr_dir_file):
            with open(adr_dir_file, "r") as file:
                adr_dir = file.read().strip()
        return adr_dir

    return maybe_dir if maybe_dir else lookup()


# fmt: off
@command()
@option('--adr-path',
              default=None,
              help=f"""
                Directory containing ADR files; pass explicitly,
                read {DEFAULT_ADR_DIR_FILE} if it exists or uses {CONVENTIONAL_ADR_DIR}
              """,
              show_default=True)
@option('--output',        default='index.html', help='File to write output to.',                show_default=True)
@option('--title',         default=None,         help='Set the project title',                   show_default=True)
@option('--serve',         default=False,        help='Serve content at http://localhost:8000/', is_flag=True)
@option('--port',          default=8000,         help='Change port for the server',              show_default=True)
@option('--template-dir',  default=None,         help='Template directory.',                     show_default=True)
# fmt: on
def main(adr_path, output, title, serve, port, template_dir) -> None:
    adr_path = resolve_adr_dir(adr_path)
    adrs: List[Adr] = parse_adr_files("%s/*.md" % adr_path)

    content = generate_content(adrs, template_dir, title)

    if serve:
        run_server(content, port)
    else:
        with open(output, "w") as out:
            out.write(content)
