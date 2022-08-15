# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.3.0](https://pypi.org/project/adr-viewer/1.3.0/) - 2022-02-28

### Added
- Ignore badly-formed ADR files and report
- Allow template override and pass in a teplate directory
- Customizing server port

### Fixed
- Some typos

### Removed
- Support for Python 2.7

## [1.2.0](https://pypi.org/project/adr-viewer/1.2.0/) - 2019-06-19

### Added
- Support for Pending ADRs

## [1.1.1](https://pypi.org/project/adr-viewer/1.1.1/) - 2019-02-26

### Added
- Python 3 support


### Fixed
- Included HTML file in package

## [1.1.0](https://pypi.org/project/adr-viewer/1.1.0/) - 2018-09-10

### Added
- Pypi release details
- Accepted records are green
- Superceded records are now grey and have their titles struck through
- Records with unknown state default to white
- Amended records are yellow
- Since multiple statuses are possible in ADR files, we now extract all `p` objects below the Status header and use those for deciding on which style to apply
- Statuses also now represented by icons (colour-blindness)
- Created and updated this project's ADRs and visualised them
- Improved `README.md`

## [1.0.1](https://pypi.org/project/adr-viewer/1.0.1/) - 2018-09-02

### Added
- Classifiers to `setup.py`


## [1.0.0](https://pypi.org/project/adr-viewer/1.0.0/) - 2018-09-02

### Initial Release

