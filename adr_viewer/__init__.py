import glob
import os
from typing import List

from click import option, command

from adr_viewer.parse import parse_adr
from adr_viewer.render import render_html, AdrTemplateConfig
from adr_viewer.server import run_server


def get_adr_files(path) -> List[str]:
    files = glob.glob(path)
    files.sort()
    return files


def generate_content(path, template_dir_override=None, title=None) -> str:
    files = get_adr_files("%s/*.md" % path)

    config = AdrTemplateConfig(
        project_title=title if title else os.path.basename(os.getcwd()), records=[]
    )

    for index, adr_file in enumerate(files):
        markdown = open(adr_file).read()
        adr = parse_adr(markdown)

        if adr:
            adr.index = index
            adr.includes_mermaid |= config.include_mermaid

            config.records.append(adr)
        else:
            print("Could not parse %s in ADR format, ignoring." % adr_file)

    return render_html(config, template_dir_override)


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
    content = generate_content(adr_path, template_dir, title)

    if serve:
        run_server(content, port)
    else:
        with open(output, "w") as out:
            out.write(content)
