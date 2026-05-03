========
Overview
========
{{ cookiecutter.project_name }} [v-{{ cookiecutter.version }}]

{% if cookiecutter.repo_hosting_domain == "github.com" %}
.. start-badges

.. list-table::
    :stub-columns: 1
{% if cookiecutter.sphinx_docs == "yes" %}
    * - docs
      - |docs|
{%- endif %}
    * - tests
{{ '' }}
{{ '' }}
{%- if cookiecutter.sphinx_docs == "yes" -%}
{%- if 'readthedocs' in cookiecutter.sphinx_docs_hosting -%}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/
    :alt: Documentation Status
{%- elif 'gitlab' in cookiecutter.sphinx_docs_hosting and 'gitlab' in cookiecutter.repo_hosting_domain -%}
.. |docs| image:: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badges/{{ cookiecutter.repo_main_branch }}/pipeline.svg
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name|replace('.', '') }}/commits/{{ cookiecutter.repo_main_branch }}
    :alt: Documentation Status
{% endif %}
{% endif %}

{%- if cookiecutter.repo_hosting_domain == "github.com" %}
.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :alt: Commits since latest release
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...{{ cookiecutter.repo_main_branch }}
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

    pip install {{ cookiecutter.distribution_name }}

You can also install the in-development version with::
{% if cookiecutter.repo_hosting_domain == "github.com" %}
    pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.repo_main_branch }}.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
    pip install https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/{{ cookiecutter.repo_main_branch }}/{{ cookiecutter.repo_name }}-{{ cookiecutter.repo_main_branch }}.zip
{% else %}
    pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@{{ cookiecutter.repo_main_branch }}
{%- endif %}

Documentation
=============

{% if cookiecutter.sphinx_docs == "yes" %}
{{ cookiecutter.sphinx_docs_hosting }}
{% else %}
To use the project:

.. code-block:: python

    import {{ cookiecutter.package_name }}
    print({{ cookiecutter.package_name }}.__version__)
{% endif %}

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
