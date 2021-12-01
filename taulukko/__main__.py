# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long,missing-module-docstring
import sys

from taulukko.cli import app

if __name__ == '__main__':
    sys.exit(app(prog_name='taulukko'))  # pragma: no cover
