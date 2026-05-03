from typer.testing import CliRunner

from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.cli import app

runner = CliRunner()


def test_main() -> None:
    result = runner.invoke(app, [])
    assert result.output == "()\n"
    assert result.exit_code == 0


def test_version() -> None:
    assert tuple(map(int, __version__.split("."))) == ({{ cookiecutter.version | replace(".", ", ") }})
