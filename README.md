# adr-viewer

[![Latest Version](https://img.shields.io/pypi/v/adr-viewer)](https://pypi.org/project/adr-viewer/)

Show off your Architecture Decision Records with an easy-to-navigate web page, either as a local web-server or generated static content.
Include diagrams in [Mermaid](https://mermaid.js.org) format using code blocks/fences, e.g. [test ADR 5](test/adr/0005-has-mermaid.md).

## Examples

<img src="https://github.com/mrwilson/adr-viewer/raw/master/images/example.png" height="500px"/>

* Example above using Nat Pryce's [adr-tools](https://github.com/npryce/adr-tools) project
* This project exposes its own Architecture Decision Records [here](https://mrwilson.github.io/adr-viewer/index.html)

## Installation

### From PyPI

```bash
$ pip install adr-viewer
```

### From Homebrew

```bash
$ brew install adr-viewer
```

See also the [`adr-viewer` formula page](https://formulae.brew.sh/formula/adr-viewer).

### From local build

adr-viewer requires Python 3.7 or higher (with Pip)

```bash
$ git clone https://github.com/mrwilson/adr-viewer
$ pip install -r requirements.txt
$ python setup.py install
```

## Usage

```bash
Usage: adr-viewer [OPTIONS]

Options:
  --adr-path TEXT      Directory containing ADR files; pass explicitly, read
                       .adr-dir if it exists or uses doc/adr/
  --output TEXT        File to write output to.  [default: index.html]
  --title TEXT         The project title   [default: the basename of the current directory]
  --serve              Serve content at http://localhost:8000/
  --port INTEGER       Change port for the server  [default: 8000]
  --template-dir TEXT  Template directory.
  --help               Show this message and exit.
```

The default for `--adr-path` is `doc/adr/` because this is the default path generated by `adr-tools`.
If `.adr-dir` exists in the directory in which `adr-viewer` was executed, it will be read and used for the `--adr-path`,
following the `adr-tools` convention for overrides.

## Supported Record Types

<img src="https://github.com/mrwilson/adr-viewer/raw/master/images/record_types.png"/>
