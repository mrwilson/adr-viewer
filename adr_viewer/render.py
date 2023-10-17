import os
from dataclasses import dataclass
from typing import List

from jinja2 import Environment, PackageLoader, select_autoescape
from jinja2.loaders import FileSystemLoader, BaseLoader

from adr_viewer.parse import Adr


@dataclass
class AdrTemplateConfig:
    project_title: str
    records: List[Adr]
    include_mermaid: bool = False


def render_html(config: AdrTemplateConfig, template_dir_override=None) -> str:
    loader: BaseLoader

    if template_dir_override:
        loader = FileSystemLoader(template_dir_override)
    else:
        loader = PackageLoader("adr_viewer", "templates")

    env = Environment(
        loader=loader,
        autoescape=select_autoescape(["html", "xml"]),
    )

    template = env.get_template("index.html")

    return template.render(config=config)


def generate_content(adrs: List[Adr], template_dir_override=None, title=None) -> str:
    config = AdrTemplateConfig(
        project_title=title if title else os.path.basename(os.getcwd()), records=[]
    )

    for index, adr in enumerate(adrs):
        adr.index = index
        adr.includes_mermaid |= config.include_mermaid

        config.records.append(adr)

    return render_html(config, template_dir_override)
