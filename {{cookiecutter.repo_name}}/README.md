<div align="center">
    <p>
        <img src="./data/logo/logo.png">
    </p>

<h2 align="center">{{ cookiecutter.repo_name }}</h4>
<h4 align="center">{{ cookiecutter.project_short_description }}</h4>
<h5 align="center">[v-{{ cookiecutter.version }}]</h5>

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#installation">Installation</a> •
  <a href="#installation">Documentation</a> •
  <a href="#installation">Development</a>
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

The documentation `code` documentation is in `build/docs`.

# Development

To run all the tests and to build the `code` documentation run

```cmd
>>> tox
```

Note, to combine the coverage data from all the tox environments run:

```cmd
>>> set PYTEST_ADDOPTS=--cov-append
>>> tox
```

for Windows and

```cmd
>>> PYTEST_ADDOPTS=--cov-append tox
```

for Linux.
