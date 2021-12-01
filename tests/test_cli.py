# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import click
import pytest

import taulukko.cli as cli


def test_main_legacy_ok(capsys):
    inp = str(pathlib.Path('tests', 'fixtures', 'basic', '2x2-table-w-th.html'))
    assert cli.main(['extract', inp]) == 0
    out, err = capsys.readouterr()
    assert 'extracting html tables from' in out.lower()
    assert not err


def test_version_ok(capsys):
    with pytest.raises(click.exceptions.Exit) as exec_info:
        cli.app_version() == 0
        assert exec_info.value.code == 0
        out, err = capsys.readouterr()
        assert 'version' in out.lower()
        assert not err


def test_extract_ok(capsys):
    in_path = pathlib.Path('tests', 'fixtures', 'basic', '2x2-table-w-th.html')
    with pytest.raises(SystemExit) as exec_info:
        cli.extract(source=in_path, inp=in_path)
        assert exec_info.value.code == 0
        out, err = capsys.readouterr()
        assert 'would extract html tables' in out.lower()
        assert not err


def test_translate_non_existing_html(capsys):
    in_path = pathlib.Path('does', 'not', 'exist', 'hypothetical.html')
    with pytest.raises(SystemExit) as exec_info:
        cli.extract(source=in_path, inp=in_path)
        assert exec_info.value.code == 1
        out, err = capsys.readouterr()
        assert 'source' in out.lower()
        assert 'is no file' in out.lower()
        assert not err
