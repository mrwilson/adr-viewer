from adr_viewer import parse_adr


def test_should_extract_title_from_record():
    markdown = open("doc/adr/0001-record-architecture-decisions.md").read()
    adr = parse_adr(markdown)

    assert adr.title == "1. Record architecture decisions"


def test_should_extract_status_from_record():
    markdown = open("doc/adr/0001-record-architecture-decisions.md").read()
    adr = parse_adr(markdown)

    assert adr.status == "accepted"


def test_should_include_adr_as_markdown():
    markdown = open("doc/adr/0001-record-architecture-decisions.md").read()
    adr = parse_adr(markdown)

    assert "<h1>1. Record architecture decisions</h1>" in adr.body


def test_should_mark_superseded_records():
    markdown = open("doc/adr/0003-use-same-colour-for-all-headers.md").read()
    adr = parse_adr(markdown)

    assert adr.status == "superseded"


def test_should_mark_amended_records():
    markdown = open("doc/adr/0004-distinguish-superseded-records-with-colour.md").read()
    adr = parse_adr(markdown)

    assert adr.status == "amended"


def test_should_mark_unknown_records():
    markdown = open("test/adr/0001-unknown-status.md").read()
    adr = parse_adr(markdown)

    assert adr.status == "unknown"


def test_should_mark_pending_records():
    markdown = open("test/adr/0002-pending-status.md").read()
    adr = parse_adr(markdown)

    assert adr.status == "pending"


def test_should_mark_pproposed_records():
    markdown = open("test/adr/0004-proposed-status.md").read()
    adr = parse_adr(markdown)

    assert adr.status == "pending"


def test_should_ignore_invalid_files():
    markdown = open("test/adr/0003-bad-formatting.md").read()
    adr = parse_adr(markdown)

    assert adr is None


def test_should_detect_mermaid():
    markdown = open("test/adr/0005-has-mermaid.md").read()
    adr = parse_adr(markdown)

    assert adr.includes_mermaid


def test_should_not_detect_mermaid():
    markdown = open("test/adr/0004-proposed-status.md").read()
    adr = parse_adr(markdown)

    assert not adr.includes_mermaid
