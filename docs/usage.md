# Example Usage

## Extract tables from local HTML file

```console
$ taulukko extract tests/fixtures/basic/2x2-table-w-th.html
extracting html tables from (tests/fixtures/basic/2x2-table-w-th.html) into markdown file below taulukko-md
markdown tree is below (taulukko-md)
```

```console
$ cat tests/fixtures/basic/2x2-table-w-th.html
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
Table (Finnish Taulukko) glued together to transform into hands-free living. version 2021.12.1
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
