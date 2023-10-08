from adr_viewer import render_html
from adr_viewer.parse import Adr


def test_should_render_html_with_project_title():
    html = render_html({"project_title": "my-project"})

    assert "<title>ADR Viewer - my-project</title>" in html


def test_should_render_html_with_record_status():
    adr = Adr("title", "accepted", "content")
    html = render_html({"records": [adr]})

    assert '<div class="panel-heading adr-accepted">' in html


def test_should_render_html_with_record_body():
    adr = Adr("title", "status", "<h1>This is my ADR</h1>")

    html = render_html({"records": [adr]})

    assert '<div class="panel-body"><h1>This is my ADR</h1></div>' in html


def test_should_render_html_with_collapsible_index():
    adr = Adr("Record 123", "status", "content")
    adr.index = 123

    html = render_html({"records": [adr]})

    assert '<a data-toggle="collapse" href="#collapse123">Record 123</a>' in html


def test_should_render_html_with_mermaid():
    html = render_html({"include_mermaid": True})

    assert "mermaid.min.js" in html


def test_should_render_html_without_mermaid():
    html = render_html({"include_mermaid": False})

    assert "mermaid.min.js" not in html
