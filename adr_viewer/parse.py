import glob
from typing import Iterator, Optional, List
from bs4 import BeautifulSoup
from dataclasses import dataclass

import mistune


@dataclass
class Adr:
    title: str
    status: str
    body: str
    index: int = 0
    includes_mermaid: bool = False


def extract_statuses_from_adr(page_object) -> Iterator[str]:
    status_section = page_object.find("h2", string="Status")

    if status_section and status_section.nextSibling:
        current_node = status_section.nextSibling

        while current_node.name != "h2" and current_node.nextSibling:
            current_node = current_node.nextSibling

            if current_node.name == "p":
                yield current_node.text
            elif current_node.name == "ul":
                yield from (li.text for li in current_node.children if li.name == "li")
            else:
                continue


def parse_adr_files(path: str) -> List[Adr]:
    files: List[str] = glob.glob(path)
    files.sort()

    adrs: List[Adr] = []

    for file in files:
        content = open(file).read()

        adr = parse_adr(content)

        if not adr:
            print("Could not parse %s in ADR format, ignoring." % file)
            continue

        adrs.append(adr)

    return adrs


def parse_adr(content: str) -> Optional[Adr]:
    adr_as_html = mistune.markdown(content)

    soup = BeautifulSoup(adr_as_html, features="html.parser")

    statuses = list(extract_statuses_from_adr(soup))

    if any([line.startswith("Amended by") for line in statuses]):
        status = "amended"
    elif any([line.startswith("Accepted") for line in statuses]):
        status = "accepted"
    elif any([line.startswith("Superseded by") for line in statuses]):
        status = "superseded"
    elif any(
        [line.startswith("Proposed") or line.startswith("Pending") for line in statuses]
    ):
        status = "pending"
    else:
        status = "unknown"

    header = soup.find("h1")

    includes_mermaid = (
        soup.find(name="code", attrs={"class": "language-mermaid"}) is not None
    )

    if header:
        return Adr(
            title=header.text,
            status=status,
            body=adr_as_html,
            includes_mermaid=includes_mermaid,
        )
    else:
        return None
