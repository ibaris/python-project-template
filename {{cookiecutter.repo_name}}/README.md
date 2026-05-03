<div align="center">
    <p>
        <img src="{{ cookiecutter.project_logo }}">
    </p>

<h2 align="center">{{ cookiecutter.project_name }}</h2>
<h4 align="center">{{ cookiecutter.project_short_description }}</h4>
<h5 align="center">[v-{{ cookiecutter.version }}]</h5>

<p align="center">
{% if cookiecutter.github_actions == "yes" and cookiecutter.repo_hosting_domain == "github.com" and cookiecutter.repo_username %}
  <a href="https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/actions/workflows/tests.yml">
    <img src="https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/actions/workflows/tests.yml/badge.svg?branch={{ cookiecutter.repo_main_branch }}" alt="Tests">
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
> pip install {{ cookiecutter.distribution_name }}
```

You can also install the stable version with

```cmd
{% if cookiecutter.repo_hosting_domain == "github.com" %}
>>> pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.repo_main_branch }}.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
>>> pip install https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/{{ cookiecutter.repo_main_branch }}/{{ cookiecutter.repo_name }}-{{ cookiecutter.repo_main_branch }}.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.dlr.de" %}
>>> pip install https://gitlab.dlr.de/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/{{ cookiecutter.repo_main_branch }}/{{ cookiecutter.repo_name }}-{{ cookiecutter.repo_main_branch }}.zip
{% else %}
>>> pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@{{ cookiecutter.repo_main_branch }}
{%- endif %}
```

To install the in-development version, change the branch name {{ cookiecutter.repo_main_branch }} to the other
available branch names.

# Documentation

The documentation `code` documentation is in `build/docs`.

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
