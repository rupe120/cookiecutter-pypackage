# Python Project Wizard for AWS CodeArtifact

A tool for creating skeleton Python project, built with popular develop tools and conform to best practice. The packages are setup to deploy to AWS CodeArtifact.

The template system used is [Cookiecutter].

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
* Continuous Integration/Deployment by [github actions], includes:
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

## Template Information

The Cookiecutter template starts with the `{{cookiecutter.project_slug}}`, and yes the {}s are part of the folder name.

The output of the template will be the following. We will use a `project_slug` of `my_project`.

``` console
.
└── my_project
    ├── AUTHORS.md
    ├── CONTRIBUTING.md
    ├── .coveragerc
    ├── dist
    ├── docs
    │   ├── api.md
    │   ├── authors.md
    │   ├── contributing.md
    │   ├── history.md
    │   ├── index.md
    │   ├── installation.md
    │   └── usage.md
    ├── .editorconfig
    ├── .flake8
    ├── .git
    ├── .github
    │   ├── ISSUE_TEMPLATE.md
    │   └── workflows
    │       ├── dev.yml
    │       └── release.yml
    ├── .gitignore
    ├── HISTORY.md
    ├── .isort.cfg
    ├── LICENSE
    ├── mkdocs.yml
    ├── poetry.lock
    ├── my_project
    │   ├── cli.py
    │   ├── __init__.py
    │   └── my_project.py
    ├── .pre-commit-config.yaml
    ├── pyproject.toml
    ├── pyrightconfig.json
    ├── README.md
    ├── site
    ├── tests
    │   ├── __init__.py
    │   └── test_my_project.py
    └── tox.ini
```

If you look through the contents of the `{{cookiecutter.project_slug}}` folder, you will notice that there is a `github` folder instead of a `.github` folder. This is because Cookiecutter does not process files in folders that start with a period. The renaming of this folder is done in the Cookiecutter post generation hook found in `hooks/post_gen_project.py`.

Notice the contents of top level `my_project` will contain a `.git` folder. You can set the origin in this git configuration or copy everything except that folder to an empty cloned repository of your choice. To install the pre-commit hooks, make sure to run `pre-commit install` from the root of the repository.

Follow **[Tutorial](https://innovativeSol.github.io/innovative-pip-cookiecutter-pypackage/tutorial/)** to finish other configurations.

## Credits

This repo is forked from [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage), and borrowed some updates from [ma7555](https://github.com/ma7555/cookiecutter-pypackage)

[Cookiecutter]: https://cookiecutter.readthedocs.io/en/1.7.3/
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
[AWS CodeArtifact]: https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html