from adr_viewer import parse_adr


def test_should_extract_title_from_record():
    adr = parse_adr('doc/adr/0001-record-architecture-decisions.md')

    assert adr.title == '1. Record architecture decisions'


def test_should_extract_status_from_record():
    adr = parse_adr('doc/adr/0001-record-architecture-decisions.md')

    assert adr.status == 'accepted'


def test_should_include_adr_as_html():
    adr = parse_adr('doc/adr/0001-record-architecture-decisions.md')

    assert '<h1>1. Record architecture decisions</h1>' in adr.body


def test_should_mark_superseded_records():
    adr = parse_adr('doc/adr/0003-use-same-colour-for-all-headers.md')

    assert adr.status == 'superseded'


def test_should_mark_amended_records():
    adr = parse_adr('doc/adr/0004-distinguish-superseded-records-with-colour.md')

    assert adr.status == 'amended'


def test_should_mark_unknown_records():
    adr = parse_adr('test/adr/0001-unknown-status.md')

    assert adr.status == 'unknown'


def test_should_mark_pending_records():
    adr = parse_adr('test/adr/0002-pending-status.md')

    assert adr.status == 'pending'


def test_should_mark_pproposed_records():
    adr = parse_adr('test/adr/0004-proposed-status.md')

    assert adr.status == 'pending'


def test_should_ignore_invalid_files():
    adr = parse_adr('test/adr/0003-bad-formatting.md')

    assert adr is None
