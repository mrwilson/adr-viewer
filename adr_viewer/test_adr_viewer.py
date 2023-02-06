# Import system modules
import os
import sys
from ast import literal_eval

import pytest
sys.path.insert(1, '..' + os.sep + 'adr_viewer')

from adrviewer import parse_adr_to_config, render_html  # noqa


@pytest.fixture
def adr0001():
    return '../doc/adr/0001-record-architecture-decisions.md'


@pytest.fixture
def html_defaults():
    defaults = literal_eval("{'page': {'background-color': 'blue'}," +
                            "'accepted': {'icon': 'fa-check', " +
                            "'background-color': 'lightgreen'}," +
                            "'amended': { 'icon': 'fa-arrow-down'," +
                            "'background-color': 'yellow'}," +
                            "'pending': { 'icon': 'fa-hourglass-half'," +
                            "'background-color': 'lightblue'}," +
                            "'superseded': {'icon': 'fa-times'," +
                            "'background-color': 'lightgrey'," +
                            "'text-decoration': 'line-through'}," +
                            "'unknown': {'icon': 'fa-question'," +
                            "'background-color': 'white'}}")
    return defaults


def test_should_extract_title_from_record(adr0001):
    config = parse_adr_to_config(adr0001)

    assert config['title'] == '1. Record architecture decisions'


def test_should_extract_status_from_record(adr0001):
    config = parse_adr_to_config(adr0001)

    assert config['status'] == 'accepted'


def test_should_include_adr_as_html(adr0001):
    config = parse_adr_to_config(adr0001)

    assert '<h1>1. Record architecture decisions</h1>' in config['body']


def test_should_mark_superseded_records():
    config = parse_adr_to_config(
        '../doc/adr/0003-use-same-colour-for-all-headers.md')

    assert config['status'] == 'superseded'


def test_should_mark_amended_records():
    adr0004 = '../doc/adr/0004-distinguish-superseded-records-with-colour.md'
    config = parse_adr_to_config(adr0004)

    assert config['status'] == 'amended'


def test_should_mark_unknown_records():
    config = parse_adr_to_config('../test/adr/0001-unknown-status.md')

    assert config['status'] == 'unknown'


def test_should_mark_pending_records():
    config = parse_adr_to_config('../test/adr/0002-pending-status.md')

    assert config['status'] == 'pending'


def test_should_render_html_with_project_title(html_defaults):
    content = {
        'heading': 'my-project'
        }
    content.update(html_defaults)
    html = render_html(content)
    assert '<title>my-project</title>' in html


def test_should_render_html_with_record_status(html_defaults):
    content = {
        'records': [{
            'status': 'accepted',
        }]
    }
    content.update(html_defaults)
    html = render_html(content)

    assert '<div class="panel-heading adr-accepted">' in html


def test_should_render_html_with_record_body(html_defaults):
    content = {
        'records': [{
            'body': '<h1>This is my ADR</h1>',
        }]
    }
    content.update(html_defaults)
    html = render_html(content)

    assert '<div class="panel-body"><h1>This is my ADR</h1></div>' in html


def test_should_render_html_with_collapsible_index(html_defaults):
    content = {
        'records': [{
            'title': 'Record 123',
            'index': 123
        }]
    }
    content.update(html_defaults)
    html = render_html(content)
    result = '<a data-toggle="collapse" href="#collapse123">Record 123</a>'
    assert result in html


def test_should_ignore_invalid_files():
    config = parse_adr_to_config('../test/adr/0003-bad-formatting.md')

    assert config is None
