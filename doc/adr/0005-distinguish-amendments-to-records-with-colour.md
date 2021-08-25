# 5. Distinguish amendments to records with colour

Date: 2018-09-09

## Status

Accepted

Amends [4. Distinguish superseded records with colour](0004-distinguish-superseded-records-with-colour.md)

## Context

Architecture Decision Records may be `amended` rather than `superseded` if e.g. only a small part of the decision changes.

## Decision

Amended records, although not officially supported as a distinct flag in `adr-tools`, should be distinguished from records that are either Accepted or Superseded by.

## Consequences

We now have to map 4 kinds of status to different formatting options, which presents a refactoring opportunity.
