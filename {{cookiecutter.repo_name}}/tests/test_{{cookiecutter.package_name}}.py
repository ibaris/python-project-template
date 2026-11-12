import os
import tomllib

from typer.testing import CliRunner

from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.cli import app

runner = CliRunner()


def test_main() -> None:
    result = runner.invoke(app, [])
    assert result.output == "()\n"
    assert result.exit_code == 0


def test_version() -> None:
    project_file = os.path.join(os.path.dirname(__file__), "..", "pyproject.toml")
    with open(project_file, "rb") as source:
        project = tomllib.load(source)
    assert __version__ == project["project"]["version"]
