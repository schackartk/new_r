# new_r.py

Python program to create a new R program. Currently supports R script and Rmarkdown files.

# Description

```
$ ./new_r.py --help
usage: new_r.py [-h] [-n NAME] [-e EMAIL] [-p PURPOSE] [-f] program

Create a new R file

positional arguments:
  program               New R file name

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name for docstring (default: Kenneth Schackart)
  -e EMAIL, --email EMAIL
                        Email address (default: schackartk1@gmail.com)
  -p PURPOSE, --purpose PURPOSE
                        Purpose for docstring (default: Do some stuff)
  -f, --force           Overwrite existing (default: False)
  ```

  The template is selected based on the file extension of the given `program` name. Currently `.R` and `.Rmd` templates are supported. Accordingly, the `program` name must end with one of those extensions.

### Setting your own defaults

The defaults can be changed by creating a "~/.new_r.py" configuration file with any or all of the following fields: name, email, purpose.

For example, mine looks like:

```
$ cat ~/.new_r.py
name=Kenneth Schackart
email=schackartk1@gmail.com
```

By doing so, I do not need to use the `-e|--email`, or `-n|--name` flags to include my information in the template by default.


## Installation

Firstly, you should clone this repository:

```
$ git clone git@github.com:schackartk/new_r.git
```

Then you can copy the `new_r.py` program to any directory currently in your `$PATH`.
It's common to place programs into a directory like `/usr/local/bin`, but this often will require root priviliges.
A common workaround is to create a writable directory in your `$HOME` where you can place programs.
One option is to use `$HOME/.local` as the "prefix" for local software installations. You can copy the program there:

```
$ cp new_r.py ~/.local/bin
```

To make sure that this directory is on your `$PATH`, you can add this to your `.bash_profile` (or `.bashrc`) file:

```
export PATH=$HOME/.local/bin:$PATH
```

## Authorship:

Author: Kenneth Schackart (schackartk1@gmail.com)

Acknowledgement: The concept is adapted from [new-py](https://github.com/kyclark/new.py) by Ken Youens-Clark
