"""
Copyright (c) 2020 Jeremiah Ikosin (@ziord)
License: MIT, see LICENSE for more details
"""

from assets.info import get_info

__all__ = ('cc',)

_d = get_info()

__author__  = _d['author']
__version__ = _d['version']


