import pathlib

from typer.testing import CliRunner

import taulukko
from taulukko.cli import app

runner = CliRunner()


def test_version_ok():
    result = runner.invoke(app, ['version'])
    assert result.exit_code == 0
    assert f'version {taulukko.__version__}' in result.stdout


def test_extract_ok(capsys):
    in_path = pathlib.Path('test', 'fixtures', 'basic', '2x2-table-w-th.html')
    result = runner.invoke(app, ['extract', str(in_path), '--input', str(in_path)])
    assert result.exit_code == 0
    assert 'extracting html tables from' in result.stdout


def test_extract_non_existing_html(capsys):
    in_path = pathlib.Path('does', 'not', 'exist', 'hypothetical.html')
    result = runner.invoke(app, ['extract', str(in_path), '--input', str(in_path)])
    assert result.exit_code == 1
    assert 'is no file' in result.stdout
