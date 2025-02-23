# -*- coding: utf-8 -*-
"""
Entrypoint
==========
*Created on 16.03.2023 by Cookiecutter Python Library Template*
*Copyright (C) 2023*
*For COPYING and LICENSE details, please refer to the LICENSE file*

Entrypoint module, in case you use `python -m{{cookiecutter.package_name}}`.

Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m

"""
{%- if cookiecutter.command_line_interface == 'plain' %}
import sys
{% endif %}
from {{cookiecutter.package_name}}.cli import main

if __name__ == "__main__":
{%- if cookiecutter.command_line_interface == 'plain' %}
    sys.exit(main())
{%- else %}
    main()
{%- endif %}
