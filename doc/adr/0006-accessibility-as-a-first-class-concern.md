# 6. Accessibility as a first-class concern

Date: 2018-09-10

## Status

Accepted

## Context

This tool had, up until this point, made assumptions about how its users might interpret the information it presents (for example, using colour as the main mechanism of distinguishing record types)

## Decision

Accessibility will now be a first-class concern of this project. All future design decisions should bear this in mind.

## Consequences

A base level of accessibility testing has been integrated using [pa11y](https://github.com/pa11y/pa11y).

This project should be (at minimum) run through a screen reader and tested for usability.