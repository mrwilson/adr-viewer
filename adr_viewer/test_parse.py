from adr_viewer import parse_adr_to_config


def test_should_extract_title_from_record():
    config = parse_adr_to_config('doc/adr/0001-record-architecture-decisions.md')

    assert config['title'] == '1. Record architecture decisions'


def test_should_extract_status_from_record():
    config = parse_adr_to_config('doc/adr/0001-record-architecture-decisions.md')

    assert config['status'] == 'accepted'


def test_should_include_adr_as_html():
    config = parse_adr_to_config('doc/adr/0001-record-architecture-decisions.md')

    assert '<h1>1. Record architecture decisions</h1>' in config['body']


def test_should_mark_superseded_records():
    config = parse_adr_to_config('doc/adr/0003-use-same-colour-for-all-headers.md')

    assert config['status'] == 'superseded'


def test_should_mark_amended_records():
    config = parse_adr_to_config('doc/adr/0004-distinguish-superseded-records-with-colour.md')

    assert config['status'] == 'amended'


def test_should_mark_unknown_records():
    config = parse_adr_to_config('test/adr/0001-unknown-status.md')

    assert config['status'] == 'unknown'


def test_should_mark_pending_records():
    config = parse_adr_to_config('test/adr/0002-pending-status.md')

    assert config['status'] == 'pending'


def test_should_mark_pproposed_records():
    config = parse_adr_to_config('test/adr/0004-proposed-status.md')

    assert config['status'] == 'pending'


def test_should_ignore_invalid_files():
    config = parse_adr_to_config('test/adr/0003-bad-formatting.md')

    assert config is None
