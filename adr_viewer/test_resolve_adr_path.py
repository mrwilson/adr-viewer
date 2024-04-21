import tempfile

from adr_viewer import resolve_adr_dir


def test_resolve_adr_path_default():
    assert resolve_adr_dir() == "doc/adr/"


def test_resolve_adr_path_explicit():
    assert resolve_adr_dir("docs/adrs") == "docs/adrs"


def test_resolve_adr_path_adrdir():
    test_adr_dir_content = "just a test  "
    with tempfile.NamedTemporaryFile("w") as tmpfile:
        tmpfile.write(test_adr_dir_content)
        tmpfile.flush()
        assert (
            resolve_adr_dir(None, adr_dir_file=tmpfile.name)
            == test_adr_dir_content.strip()
        )
