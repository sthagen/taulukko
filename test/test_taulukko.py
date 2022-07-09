# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import taulukko.taulukko as tau


def test_ko_main():
    inp = str(pathlib.Path('test', 'fixtures', 'basic', '2x2-table-w-th.html'))
    assert tau.main(['extract', inp]) == 0


def test_ko_verify_request_too_few():
    assert tau.verify_request([1]) == (2, 'received wrong number of arguments', [''])


def test_ko_verify_request_unknown_command():
    assert tau.verify_request(['unknown', 'does not matter']) == (2, 'received unknown command', [''])


def test_ko_verify_request_falsy_input():
    argv = ['extract', '']
    assert tau.verify_request(argv) == (0, '', argv)
