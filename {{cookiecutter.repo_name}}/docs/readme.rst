========
Overview
========
{{ cookiecutter.project_name }} [v-{{ cookiecutter.version }}]

{% if cookiecutter.repo_hosting_domain == "github.com" %}
.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
{{ '' }}
{{ '' }}
{%- if 'readthedocs' in cookiecutter.sphinx_docs_hosting -%}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/
    :alt: Documentation Status
{%- elif 'gitlab' in cookiecutter.sphinx_docs_hosting and 'gitlab' in cookiecutter.repo_hosting_domain -%}
.. |docs| image:: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badges/main/pipeline.svg
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name|replace('.', '') }}/commits/main
    :alt: Documentation Status
{% endif %}

{%- if cookiecutter.repo_hosting_domain == "github.com" %}
.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :alt: Commits since latest release
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...main
{% endif %}

.. end-badges
{% endif %}
{{ cookiecutter.project_short_description|wordwrap(119) }}
{% if cookiecutter.license != "no" %}
* Free software: {{ cookiecutter.license }}
{% endif %}
Installation
============

::

    pip install {{ cookiecutter.package_name }}

You can also install the in-development version with::
{% if cookiecutter.repo_hosting_domain == "github.com" %}
    pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/main.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
    pip install https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/main/{{ cookiecutter.repo_name }}-main.zip
{% else %}
    pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@main
{%- endif %}

Documentation
=============

{{ cookiecutter.sphinx_docs_hosting }}

Development
===========

Install the project in editable mode with the development dependencies::

    pip install -e .[dev]

Run the test suite directly with::

    pytest

Run linting and formatting with::

    python -m ruff check --fix .
    python -m ruff format .

To include coverage use::

    pytest --cov --cov-report=term-missing
