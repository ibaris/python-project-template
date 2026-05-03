"""Package metadata for {{ cookiecutter.project_name }}."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ cookiecutter.distribution_name }}")
except PackageNotFoundError:
    __version__ = "{{ cookiecutter.version }}"
