"""
:copyright: Copyright (c) 2020 Jeremiah Ikosin (@ziord)
:license: MIT, see LICENSE for more details
"""

import os
import importlib.util as iutil
import sys

fp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
info_py = os.path.join(fp, 'info.py')
spec = iutil.spec_from_file_location('info', info_py)
info = iutil.module_from_spec(spec)
spec.loader.exec_module(info)

from info import get_info

__all__ = ('cc',)

_d = get_info()
__author__  = _d['author']
__version__ = _d['version']




