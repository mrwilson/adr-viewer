from adr_viewer import generate_configuration, render_html, AdrTemplateConfig
from adr_viewer.parse import Adr


def test_should_render_html_with_project_title():
    html = render_html(AdrTemplateConfig(project_title="my-project", records=[]))

    assert "<title>ADR Viewer - my-project</title>" in html


def test_should_render_html_with_record_status():
    adr = Adr("title", "accepted", "content")
    html = render_html(AdrTemplateConfig(project_title="my-project", records=[adr]))

    assert '<div class="panel-heading adr-accepted">' in html


def test_should_render_html_with_record_body():
    adr = Adr("title", "status", "<h1>This is my ADR</h1>")

    html = render_html(AdrTemplateConfig(project_title="my-project", records=[adr]))

    assert '<div class="panel-body"><h1>This is my ADR</h1></div>' in html


def test_should_render_html_with_collapsible_index():
    adr = Adr("Record 123", "status", "content")
    adr.index = 123

    html = render_html(AdrTemplateConfig(project_title="my-project", records=[adr]))

    assert '<a data-toggle="collapse" href="#collapse123">Record 123</a>' in html


def test_should_render_html_with_mermaid():
    html = render_html(
        AdrTemplateConfig(project_title="my-project", records=[], include_mermaid=True)
    )

    assert "mermaid.min.js" in html


def test_should_render_html_without_mermaid():
    html = render_html(
        AdrTemplateConfig(project_title="my-project", records=[], include_mermaid=False)
    )

    assert "mermaid.min.js" not in html


def test_should_add_mermaid_dependency_to_overall_render():
    adr = Adr("Record 123", "status", "content")
    adr.includes_mermaid = True

    config = generate_configuration(adrs=[adr], title="title")

    assert config.include_mermaid


def test_should_not_add_mermaid_dependency_to_overall_render_if_not_needed():
    adr = Adr("Record 123", "status", "content")

    config = generate_configuration(adrs=[adr], title="title")

    assert not config.include_mermaid

def test_should_render_html_with_theme_support():
    html = render_html(
        AdrTemplateConfig(project_title="my-project", records=[])
    )

    # Check that CSS variables for theming are defined
    assert '--bg-color:' in html
    assert '--text-color:' in html
    assert '[data-theme="dark"]' in html

    # Check that toggle button is present
    assert 'id="theme-toggle"' in html
    assert 'theme-toggle' in html

    # Check that JavaScript for theme switching is included
    assert 'setTheme' in html
    assert 'localStorage.getItem(\'theme\')' in html