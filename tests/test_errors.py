"""
:copyright: Copyright (c) 2020 Jeremiah Ikosin (@ziord)
:license: MIT, see LICENSE for more details
"""


interrclone = """
>>> from spy.cc import clone, BuiltinTypeNotSupportedException
>>> try:
...     @clone(int)
...     class IntErrorClone:
...         pass
... except Exception as e:
...     print(isinstance(e, BuiltinTypeNotSupportedException))
...
True
"""

listerrclone = """
>>> from spy.cc import clone, BuiltinTypeNotSupportedException
>>> try:
...     @clone(str)
...     class ListErrorClone:
...         pass
... except Exception as e:
...     print(isinstance(e, BuiltinTypeNotSupportedException))
...
True
"""

__test__ = {
    'interrclone': interrclone,
    'listerrclone': listerrclone
}


if __name__ == '__main__':
    import doctest
    doctest.testmod()