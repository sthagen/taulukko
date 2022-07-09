# taulukko

[![license](https://img.shields.io/github/license/sthagen/taulukko.svg?style=flat)](https://github.com/sthagen/taulukko/blob/default/LICENSE)
[![version](https://img.shields.io/pypi/v/taulukko.svg?style=flat)](https://pypi.python.org/pypi/taulukko/)
[![downloads](https://img.shields.io/pypi/dm/taulukko.svg?style=flat)](https://pypi.python.org/pypi/taulukko/)
[![wheel](https://img.shields.io/pypi/wheel/taulukko.svg?style=flat)](https://pypi.python.org/pypi/taulukko/)
[![supported-versions](https://img.shields.io/pypi/pyversions/taulukko.svg?style=flat)](https://pypi.python.org/pypi/taulukko/)
[![supported-implementations](https://img.shields.io/pypi/implementation/taulukko.svg?style=flat)](https://pypi.python.org/pypi/taulukko/)

Table (Finnish Taulukko) glued together to transform into hands-free living.

# Installation

Preferred way to install is as usual (for testing or in isolation):

```bash
$ pipx install taulukko
```

For production use (well, ahem, ...) or within a virtual python env:

```bash
$ pip install taulukko
```

# Example Usage

## Extract tables from local HTML file

```console
$ taulukko extract test/fixtures/basic/2x2-table-w-th.html
extracting html tables from (test/fixtures/basic/2x2-table-w-th.html) into markdown file below taulukko-md
markdown tree is below (taulukko-md)
```

```console
$ cat test/fixtures/basic/2x2-table-w-th.html
<html><head><title>test</test></head><body><table><tr><th>a</th><th>b</th></tr><tr><td>c</td><td>d</td></tr></table></body></html>
```

```console
$ cat taulukko-md/collected-tables.md
# test_html1
|  a  |  b  |
| --- | --- |
| c   | d   |
```

## Version command

```console
$ taulukko version
Table (Finnish Taulukko) glued together to transform into hands-free living. version 2021.12.2
```

## General help

```console
$ taulukko
Usage: taulukko [OPTIONS] COMMAND [ARGS]...

  Table (Finnish Taulukko) glued together to transform into hands-free living.

  Given an html file or URL the tool produces a markdown file of the tables
  below `taulukko-md`.

Options:
  -V, --version  Display the taulukko version and exit
  -h, --help     Show this message and exit.

Commands:
  extract  Translate from zip file containing a tree of html and media...
  version  Display the taulukko version and exit
```

## Help on extract command

```console
$ taulukko extract --help
Usage: taulukko extract [OPTIONS] [SOURCE]

  Translate from zip file containing a tree of html and media files to a
  folder with markdown.

Arguments:
  [SOURCE]  [default: STDIN]

Options:
  -i, --input <sourcepath>  Path to input file (default is reading from
                            standard in)
  -h, --help                Show this message and exit.
```

## Help on version command

Why not :-)

```console
$ taulukko version --help
Usage: taulukko version [OPTIONS]

  Display the taulukko version and exit

Options:
  -h, --help  Show this message and exit.
```

## Status

Experimental.

**Note**: The default branch is `default`.

