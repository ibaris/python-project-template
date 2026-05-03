# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project uses calendar versioning in the `YYYY.MM.INC0.PATCH` format.

{% set datestring -%}
{% if cookiecutter.release_date == 'today' -%}
{% now 'utc', '%Y-%m-%d' %}
{%- else %}{{ cookiecutter.release_date }}{% endif %}
{%- endset %}

## [{{ cookiecutter.version }}] - ({{ datestring }})

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security
