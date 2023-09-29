from adr_viewer import render_html


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
