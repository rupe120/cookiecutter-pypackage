# Python Project Wizard for AWS CodeArtifact

A tool for creating skeleton Python project, built with popular develop tools and conform to best practice. The packages are setup to deploy to AWS CodeArtifact.

[![CI Status](https://github.com/innovativeSol/innovative-pip-cookiecutter-pypackage/actions/workflows/release.yml/badge.svg)](https://github.com/innovativeSol/innovative-pip-cookiecutter-pypackage)

## Features

This tool will create Python project with the following features:

* [Poetry]: Manage version, dependancy, build and release
* [Mkdocs]: Writting your docs in markdown style
* Testing with [Pytest] (unittest is still supported out of the box)
* Code coverage report and endorsed by [Codecov]
* [Tox]: Test your code against environment matrix, lint and artifact check.
* Format with [Black] and [Isort]
* Lint code with [Flake8] and [Flake8-docstrings]
* [Pre-commit hooks]: Formatting/linting anytime when commit/run local tox/CI
* [Mkdocstrings]: Auto API doc generation
* Command line interface using [Python Fire] (optional)
* Continuouse Integration/Deployment by [github actions], includes:
  * publish dev build/official release to [AWS CodeArtifact] automatically when CI success
  * publish documents automatically when CI success
  * extract change log from github and integrate with release notes automatically
* Host your documentation from [Git Pages] with zero-config

## Quickstart

Install aws-ppw if you haven't install it yet:

``` console
  pip install -U git+https://github.com/innovativeSol/innovative-pip-cookiecutter-pypackage
```

Generate a Python package project by simple run:

``` console
  aws-ppw
```

Then follow **[Tutorial](https://innovativeSol.github.io/innovative-pip-cookiecutter-pypackage/tutorial/)** to finish other configurations.

## Credits

This repo is forked from [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage), and borrowed some updates from [ma7555](https://github.com/ma7555/cookiecutter-pypackage)

[poetry]: https://python-poetry.org/
[mkdocs]: https://www.mkdocs.org
[pytest]: https://pytest.org
[codecov]: https://codecov.io
[tox]: https://tox.readthedocs.io
[black]: https://github.com/psf/black
[isort]: https://github.com/PyCQA/isort
[flake8]: https://flake8.pycqa.org
[flake8-docstrings]: https://pypi.org/project/flake8-docstrings/
[mkdocstrings]: https://mkdocstrings.github.io/
[Python Fire]: https://github.com/google/python-fire
[github actions]: https://github.com/features/actions
[Git Pages]: https://pages.github.com
[Pre-commit hooks]: https://pre-commit.com/
[AWS CodeArtifact] https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html