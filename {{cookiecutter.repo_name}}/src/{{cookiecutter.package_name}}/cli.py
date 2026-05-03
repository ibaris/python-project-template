"""
Command Line Interface
======================
*Created on 16.03.2023 by Cookiecutter Python Library Template*
*Copyright (C) 2023*
*For COPYING and LICENSE details, please refer to the LICENSE file*

Module that contains the command line app. Why does this file exist, and why not put this in __main__?

You might be tempted to import things from __main__ later, but that will cause
problems: the code will get executed twice:

- When you run `python -m{{cookiecutter.package_name}}` python will execute
  ``__main__.py`` as a script. That means there won't be any
  ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.

The Typer app lives in this module so it can be reused by both the console
script entry point and `python -m {{cookiecutter.package_name}}`.
"""

from typing import Annotated

import typer

app = typer.Typer(help="Command line interface for {{ cookiecutter.project_name }}.")


@app.command()
def main(names: Annotated[list[str] | None, typer.Argument()] = None) -> None:
    """Run the default command."""
    typer.echo(repr(tuple(names or [])))
