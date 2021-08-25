# 4. Distinguish superseded records with colour

Date: 2018-09-09

## Status

Accepted

Supercedes [3. Use same colour for all headers](0003-use-same-colour-for-all-headers.md)

Amended by [5. Distinguish amendments to records with colour](0005-distinguish-amendments-to-records-with-colour.md)

## Context

`adr-viewer` presents all records with the same `lightgreen` header, even though records may be in different states.

## Decision

Records marked as 'Superseded' will distinguish themselves from 'Accepted' 

## Consequences

We must invest time thinking about the user experience for this visual indication - whether or not simply greying out is sufficient.

We must also offer a default display if logic for processing a custom linkage does not exist in this project.
