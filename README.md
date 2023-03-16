# adr-viewer

[![Build Status](https://travis-ci.org/mrwilson/adr-viewer.svg?branch=master)](https://travis-ci.org/mrwilson/adr-viewer)

Show off your Architecture Decision Records with an easy-to-navigate web page, either as a local web-server or generated static content.

## Examples

<img src="images/example.png" height="500px"/>

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
  --adr-path TEXT  Directory containing ADR files.  [default: doc/adr/]
  --output TEXT    File to write output to.  [default: index.html]
  --title TEXT     The project title   [default: the basename of the current directory]
  --serve          Serve content at http://localhost:8000/
  --port INT       Custom server port [default: 8000]
  --help           Show this message and exit.
```

The default for `--adr-path` is `doc/adr/` because this is the default path generated by `adr-tools`.

## Supported Record Types

<img src="images/record_types.png"/>
