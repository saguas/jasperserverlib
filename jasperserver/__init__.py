__author__ = 'Luis Fernandes <luisfmfernandes@gmail.com>'
__version__ = '0.1.0'

__classifiers__ = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries',
]
__copyright__ = "2014, %s " % __author__
__license__ = """
   Copyright (C) %s

      This program is free software: you can redistribute it and/or modify
      it under the terms of the GNU General Public License as published by
      the Free Software Foundation, either version 3 of the License, or
      (at your option) any later version.

      This program is distributed in the hope that it will be useful,
      but WITHOUT ANY WARRANTY; without even the implied warranty of
      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
      GNU General Public License for more details.

      You should have received a copy of the GNU General Public License
      along with this program.  If not, see <http://www.gnu.org/licenses/>.
""" % __copyright__

import logging

LOG_LEVELS = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}

def set_logging(level, handler=None):
    if not handler:
        handler = logging.StreamHandler()
    format = r'[%(levelname)s] %(message)s'
    handler.setFormatter(logging.Formatter(format))
    loggers = [
        logging.getLogger('jasperserver'),
    ]
    for logger in loggers:
        logger.setLevel(LOG_LEVELS.get(level, logging.INFO))
        logger.addHandler(handler)
