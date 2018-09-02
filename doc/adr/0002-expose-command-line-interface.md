# 2. Expose command line interface

Date: 2018-09-02

## Status

Accepted

## Context

We want to maximise the usability of adr-viewer whilst maintaining flexibility in future for other output formats, e.g. a live webserver.

## Decision

The entry point for this project will be a command-line utility called `adr-viewer`. We will use the python [click](http://click.pocoo.org/5/) library to provide command-line options and documentation.

## Consequences

Click will be added as a dependency, and further improvements should consider the user experience of the command-line interface.