# new_r.py

Python program to create a new R program. Currently supports R script and Rmarkdown files.

# Description

```
$ ./new_r.py --help
usage: new_r.py [-h] [-t TEMPLATE] [-n NAME] [-e EMAIL] [-p PURPOSE] [-f] program

Create a new R file

positional arguments:
  program               New R file name

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        Template type (default: script)
  -n NAME, --name NAME  Name for docstring (default: ken)
  -e EMAIL, --email EMAIL
                        Email address (default: ken@localhost)
  -p PURPOSE, --purpose PURPOSE
                        Purpose for docstring (default: Do some stuff)
  -f, --force           Overwrite existing (default: False)
  ```