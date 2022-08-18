# Contributing to adr-viewer

First of all, thanks for contributing!

This is an evolving document which details what's needed to build and deploy `adr-viewer`.
Some tasks are only for maintainers, and some are for contributors.

Tasks and information for maintainers are depicted by :large_orange_diamond:
Tasks and information for contributors are depicted by :large_blue_diamond:

## Contribution Model :large_blue_diamond:

adr-viewer uses the "Gitflow" model (as show in the diagram below). This means that contributors can be working on different branches and features simultaneously, whilst still knowing that there is a path toward production for their contributions, be they code or documentation.

<img src="images/gitflow.png" />

Note that for this model to function correctly, branches must be named accordingly, since the build infrastructure uses these names to determine what to build, and (in some cases) what to deploy and where.

**Branch names**
| Name | Description | Responsibility |
|-----|-----|:--:|
| main | This branch contains the code which is currently in production and therefore deployed to PyPI, and which will be cloned for users to use |  :large_orange_diamond: |
| hotfix | A hotfix branch is created when a major bug is detected and needs a fix to the production code immediately|:large_orange_diamond: :large_blue_diamond:|
| release | A release branch is taken when a stable codebase is about to be deployed to production. It must be stable and no further changes can be made to it post-release |:large_orange_diamond: |
|develop| This branch "collects" all the PRs that have been successfully merged, ready for a release to be cut when ready|:large_orange_diamond: |
|feature| Feature branches are where new functionality is developed, bug fixes and general updates are carried out prior to being tested and merged into the develop branch|:large_blue_diamond: |


**Making a feature change** :large_blue_diamond: :large_orange_diamond:

To allow the change process to proceed smoothly, when making a change, please do the following:

- ensure that you have forked the main repository

All instructions from here onward relate to YOUR copy of the forked repository

- create a new feature branch (e.g. feature/29 - where 29 is the issue number)
- checkout that branch locally
- make the change and add any new tests, and make sure the existing tests still pass.
- add the changed/new/deleted files to the tracked files list (git add xxxxxx)
- commit the changes with an appropriate message (stating which issue is fixed)
- push the changes into the repository
- when you are ready, create a PR into the develop branch
- collaborate on the review of the PR until the maintainer merges it into the develop branch
- this PR will then be deployed into the next release

**Secrets and Tokens** :large_orange_diamond:

In order for the build to successfully complete, the following tokens and secrets need to be defined:

SONAR_TOKEN
