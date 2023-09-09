from adr_viewer import parse_adr_to_config, render_html


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

def test_should_render_html_with_project_title():
    html = render_html({
        'project_title': 'my-project'
    })

    assert '<title>ADR Viewer - my-project</title>' in html


def test_should_render_html_with_record_status():
    html = render_html({
        'records': [{
            'status': 'accepted',
        }]
    })

    assert '<div class="panel-heading adr-accepted">' in html


def test_should_render_html_with_record_body():
    html = render_html({
        'records': [{
            'body': '<h1>This is my ADR</h1>',
        }]
    })

    assert '<div class="panel-body"><h1>This is my ADR</h1></div>' in html


def test_should_render_html_with_collapsible_index():
    html = render_html({
        'records': [{
            'title': 'Record 123',
            'index': 123
        }]
    })

    assert '<a data-toggle="collapse" href="#collapse123">Record 123</a>' in html


def test_should_ignore_invalid_files():
    config = parse_adr_to_config('test/adr/0003-bad-formatting.md')

    assert config is None
