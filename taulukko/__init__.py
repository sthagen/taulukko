"""Table (Finnish Taulukko) glued together to transform into hands-free living."""

import datetime as dti
import logging
import os
import pathlib
from typing import List, no_type_check

# [[[fill git_describe()]]]
__version__ = '2023.10.21+parent.a4c9c8aa'
# [[[end]]] (checksum: a55b7f3e21ed0acdaa7048e615ea87b2)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_ALIAS = str(pathlib.Path(__file__).parent.name)
APP_ENV = APP_ALIAS.upper()
APP_NAME = locals()['__doc__']
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = f'.{APP_ALIAS}.json'

COMMA = ','
DEFAULT_LF_ONLY = 'YES'
log = logging.getLogger()  # Module level logger is sufficient
LOG_FOLDER = pathlib.Path('logs')
LOG_FILE = f'{APP_ALIAS}.log'
LOG_PATH = pathlib.Path(LOG_FOLDER, LOG_FILE) if LOG_FOLDER.is_dir() else pathlib.Path(LOG_FILE)
LOG_LEVEL = logging.INFO

TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'
TS_FORMAT_PAYLOADS = '%Y-%m-%d %H:%M:%S.%f UTC'

__all__: List[str] = [
    'APP_ALIAS',
    'APP_NAME',
    'DEBUG',
    'log',
]


@no_type_check
def formatTime_RFC3339(self, record, datefmt=None):  # noqa
    """HACK A DID ACK we could inject .astimezone() to localize ..."""
    return dti.datetime.fromtimestamp(record.created, dti.timezone.utc).isoformat()  # pragma: no cover


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log  # pylint: disable=global-statement

    log_format = {
        'format': '%(asctime)s %(levelname)s [%(name)s]: %(message)s',
        'datefmt': TS_FORMAT_LOG,
        # 'filename': LOG_PATH,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.Formatter.formatTime = formatTime_RFC3339
    logging.basicConfig(**log_format)
    log = logging.getLogger(APP_ENV if name is None else name)
    log.propagate = True


init_logger(name=APP_ENV, level=logging.DEBUG if DEBUG else None)
