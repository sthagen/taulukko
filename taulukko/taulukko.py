# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Table (Finnish Taulukko) glued together to transform into hands-free living. API."""
import os
import pathlib
import sys
from typing import List, Optional, Tuple, Union

import pytablereader as ptr  # type: ignore
import pytablewriter as ptw

DEBUG_VAR = 'TAULUKKO_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'

STDIN, STDOUT = 'STDIN', 'STDOUT'
DISPATCH = {
    STDIN: sys.stdin,
    STDOUT: sys.stdout,
}

MD_ROOT = pathlib.Path('taulukko-md')


def verify_request(argv: Optional[List[str]]) -> Tuple[int, str, List[str]]:
    """Fail with grace."""
    if not argv or len(argv) != 2:
        return 2, 'received wrong number of arguments', ['']

    command, inp = argv

    if command not in ('extract'):
        return 2, 'received unknown command', ['']

    if inp:
        in_path = pathlib.Path(str(inp))
        if not in_path.is_file():
            return 1, f'source ({in_path}) is no file', ['']
        if not ''.join(in_path.suffixes).lower().endswith('.html'):
            return 1, 'source has not .html extension', ['']

    return 0, '', argv


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the translation."""
    error, message, strings = verify_request(argv)
    if error:
        print(message, file=sys.stderr)
        return error

    command, inp = strings

    out_root = MD_ROOT
    print(f'extracting html tables from ({inp if inp else STDIN}) into markdown file below {out_root}')
    try:
        loader = ptr.TableFileLoader(inp)
    except ptr.error.InvalidFilePathError as err:
        print(f'html file does not exist? detail: {err}')
        return 1
    writer = ptw.MarkdownTableWriter(margin=1)
    index_path = out_root / 'collected-tables.md'
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_path, 'w', encoding=loader.encoding) as handle:
        writer.stream = handle
        for table_data in loader.load():
            writer.from_tabledata(table_data)
            writer.write_table()

    print(f'markdown tree is below ({out_root})')

    return 0
