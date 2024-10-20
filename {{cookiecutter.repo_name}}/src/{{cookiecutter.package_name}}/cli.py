# -*- coding: utf-8 -*-
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

Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
{%- if cookiecutter.command_line_interface == 'click' %}
import click
{%- elif cookiecutter.command_line_interface == 'argparse' %}
import argparse
{%- else %}
from typing import Literal
import sys
{%- endif %}
{%- if cookiecutter.command_line_interface == 'click' %}


@click.command()
@click.argument('names', nargs=-1)
def main(names) -> None:
    click.echo(repr(names))
{%- elif cookiecutter.command_line_interface == 'argparse' %}

parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(args=None) -> None:
    args = parser.parse_args(args=args)
    print(args.names)
{%- else %}


def main(argv=sys.argv) -> Literal[0]:
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    print(argv)
    return 0
{%- endif %}
