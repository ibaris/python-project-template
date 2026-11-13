<div align="center">
    <p>
        <img src="{{ cookiecutter.project_logo }}">
    </p>

<h2 align="center">{{ cookiecutter.project_name }}</h2>
<h4 align="center">{{ cookiecutter.project_short_description }}</h4>
<h5 align="center">[v-{{ cookiecutter.version }}]</h5>

<p align="center">
{% if cookiecutter.github_actions == "yes" and cookiecutter.repo_hosting_domain == "github.com" and cookiecutter.repo_username %}
  <a href="https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml">
    <img src="https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml/badge.svg?branch=main" alt="Tests">
  </a>
{% endif %}
  <a href="#introduction">Introduction</a> &bull;
  <a href="#installation">Installation</a> &bull;
  <a href="#documentation">Documentation</a> &bull;
  <a href="#development">Development</a>
</p>
</div>

# Overview

{{ cookiecutter.project_short_description|wordwrap(119) }}
{% if cookiecutter.license != "no" %}

-   Free software: {{ cookiecutter.license }}
    {% endif %}

# Installation

```cmd
> pip install {{ cookiecutter.package_name }}
```

You can also install the stable version with

```cmd
{% if cookiecutter.repo_hosting_domain == "github.com" %}
>>> pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/main.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
>>> pip install https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/main/{{ cookiecutter.repo_name }}-main.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.dlr.de" %}
>>> pip install https://gitlab.dlr.de/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/main/{{ cookiecutter.repo_name }}-main.zip
{% else %}
>>> pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@main
{%- endif %}
```

To install the in-development version, change the branch name main to the other
available branch names.

# Documentation

Documentation sources are in `docs`. Build the HTML documentation with:

```cmd
python -m pip install -e ".[docs]"
python -m sphinx -b html docs build/docs
```

Open `build/docs/index.html` to read the generated documentation.

# Project structure

```text
src/
    {{ cookiecutter.package_name }}/  # Importable package and CLI
    .info/                          # Authors and changelog
docs/                               # Sphinx documentation
tests/                              # Package tests
resources/
    configs/                        # Application configuration examples
    envs/                           # Conda environment
    images/                         # Logos and documentation images
    scripts/                        # Release tooling
.github/workflows/                  # CI, versioning, and releases
```

# Development

Install the project in editable mode with the development dependencies:

```cmd
> pip install -e .[dev]
```

Run the test suite directly with `pytest`:

```cmd
> pytest
```

Run linting and formatting with Ruff:

```cmd
> python -m ruff check --fix .
> python -m ruff format .
```

To include coverage:

```cmd
> pytest --cov --cov-report=term-missing
```

Check the package import rules with `lint-imports`.

Build a release wheel in an isolated staging directory with:

```cmd
python resources/scripts/deploy.py --src . --output-dir wheelhouse
```

The script verifies the wheel and copies it into `wheelhouse`.
