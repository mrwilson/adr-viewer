from typing import Iterator, Optional, Dict
from bs4 import BeautifulSoup

import mistune


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

    includes_mermaid = soup.find(name='code', attrs={'class': 'language-mermaid'})

    if header:
        return {
            'status': status,
            'body': adr_as_html,
            'title': header.text,
            'includes_mermaid': includes_mermaid
    }
    else:
        return None