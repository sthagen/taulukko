"""Commandline API gateway for taulukko."""
import sys
from typing import List, Union

import typer

import taulukko
import taulukko.taulukko as tau

APP_NAME = 'Table (Finnish Taulukko) glued together to transform into hands-free living.'
APP_ALIAS = 'taulukko'
app = typer.Typer(
    add_completion=False,
    context_settings={'help_option_names': ['-h', '--help']},
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def callback(
    version: bool = typer.Option(
        False,
        '-V',
        '--version',
        help='Display the taulukko version and exit',
        is_eager=True,
    )
) -> None:
    """
    Table (Finnish Taulukko) glued together to transform into hands-free living.

    Given an html file or URL the tool produces a markdown file of the tables
    below `taulukko-md`.
    """
    if version:
        typer.echo(f'{APP_NAME} version {taulukko.__version__}')
        raise typer.Exit()


@app.command('extract')
def extract(
    source: str = typer.Argument(tau.STDIN),
    inp: str = typer.Option(
        '',
        '-i',
        '--input',
        help='Path to input file (default is reading from standard in)',
        metavar='<sourcepath>',
    ),
) -> int:
    """
    Translate from zip file containing a tree of html and media files to a folder with markdown.
    """
    command = 'extract'
    incoming = inp if inp else (source if source != tau.STDIN else '')
    action = [command, str(incoming)]
    return sys.exit(tau.main(action))


@app.command('version')
def app_version() -> None:
    """
    Display the taulukko version and exit
    """
    callback(True)


# pylint: disable=expression-not-assigned
# @app.command()
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    return tau.main(argv)
