from .members import *

from collections import namedtuple
import logging

__title__ = 'dsg'
__author__ = 'RainbowLegend'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 RainbowLegend'
__version__ = '0.1.0'

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=1, micro=0, releaselevel='final', serial=0)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
            
logging.getLogger(__name__).addHandler(NullHandler())
