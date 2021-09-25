#!/usr/bin/env python3
"""
Author : Kenneth Schackart <schackartk1@gmail.com>
Purpose: Python program to create new R files
"""

import argparse
import os
import platform
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

from typing import NamedTuple, Optional, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    program: str
    name: str
    email: str
    purpose: str
    template: str
    overwrite: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get arguments """

    parser = argparse.ArgumentParser(
        prog='new_r.py',
        description='Create a new R file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    rc_file = os.path.join(str(Path.home()), '.new_r.py')
    defaults = get_defaults(open(rc_file) if os.path.isfile(rc_file) else None)
    username = os.getenv('USER') or 'Anonymous'
    hostname = os.getenv('HOSTNAME') or 'localhost'

    parser.add_argument('program', help='New R file name', type=str)

    parser.add_argument('-t',
                        '--template',
                        type=str,
                        default=defaults.get('template', 'script'),
                        help='Template type')

    parser.add_argument('-n',
                        '--name',
                        type=str,
                        default=defaults.get('name', username),
                        help='Name for docstring')

    parser.add_argument('-e',
                        '--email',
                        type=str,
                        default=defaults.get('email',
                                             f'{username}@{hostname}'),
                        help='Email address')

    parser.add_argument('-p',
                        '--purpose',
                        type=str,
                        default=defaults.get('purpose', 'Do some stuff'),
                        help='Purpose for docstring')

    parser.add_argument('-f',
                        '--force',
                        help='Overwrite existing',
                        action='store_true')

    args = parser.parse_args()

    args.program = args.program.strip().replace('-', '_')

    if not args.program:
        parser.error(f'Not a usable filename "{args.program}"')

    _, file_extension = os.path.splitext(args.program)

    if file_extension == '.Rmd':
        args.template = 'markdown'
    elif file_extension == '.R':
        args.template = 'script'

    if args.template.lower() in ['rmd', 'md', 'rmarkdown', 'rmd']:
        args.template = 'markdown'
    elif args.template.lower() == 'r':
        args.template = 'script'
    
    if args.template not in ['script', 'markdown']:
        parser.error(f'--template "{args.template}" not recognized')

    return Args(program=args.program,
                template=args.template,
                name=args.name,
                email=args.email,
                purpose=args.purpose,
                overwrite=args.force)


# --------------------------------------------------
def main() -> None:
    """ The good stuff """

    args = get_args()
    program = args.program

    if os.path.isfile(program) and not args.overwrite:
        answer = input(f'"{program}" exists.  Overwrite? [yN] ')
        if not answer.lower().startswith('y'):
            sys.exit('Will not overwrite. Bye!')

    if args.template == 'script':
        content = get_script(args)
    elif args.template == 'markdown':
        content = get_rmd(args)

    print(content, file=open(program, 'wt'), end='')

    if platform.system() != 'Windows':
        subprocess.run(['chmod', '+x', program], check=True)

    print(f'Done, see new script "{program}".')


# --------------------------------------------------
def get_script(args: Args) -> str:
    """ R script template """

    return f"""#!/usr/bin/env Rscript

# Author : {args.name}{' <' + args.email + '>' if args.email else ''}
# Date   : {str(date.today())}
# Purpose: {args.purpose}

# Imports -------------------------------------------------------------------

## Library calls ------------------------------------------------------------

library(magrittr)

## File imports -------------------------------------------------------------

source("src/config.R")

"""


# --------------------------------------------------
def get_rmd(args: Args) -> str:
    """ Rmarkdown tempalte """

    return f"""---
title: "{args.program}"
author: "{args.name}{' <' + args.email + '>' if args.email else ''}"
date: "{str(date.today())}"
output: html_document
---

## Purpose
{args.purpose}

```{{r setup, echo = FALSE}}
library(magrittr)
```

```{{r imports, echo = FALSE}}
source("src/config.R")
```

## Inline formatting

_This_ and *this* are italic.

**This** is bold

Here is a sub~script~

Here is some `inline code`

Even inline LaTeX can be used like $f(k) = {{n \choose k}} p^{{k}} (1-p)^{{n-k}}$

"""


# --------------------------------------------------
def get_defaults(file_handle: Optional[TextIO]):
    """ Get defaults from ~/.new_r.py """

    defaults = {}
    if file_handle:
        for line in file_handle:
            match = re.match('([^=]+)=([^=]+)', line)
            if match:
                key, val = map(str.strip, match.groups())
                if key and val:
                    defaults[key] = val

    return defaults


# --------------------------------------------------
if __name__ == '__main__':
    main()