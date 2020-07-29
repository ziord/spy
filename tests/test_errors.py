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
... except BuiltinTypeNotSupportedException as e:
...     print(e)
...
Cannot clone builtin type: int
"""

strerrclone = """
>>> from spy.cc import clone, BuiltinTypeNotSupportedException
>>> try:
...     @clone(str)
...     class ListErrorClone:
...         pass
... except BuiltinTypeNotSupportedException as e:
...     print(e)
...
Cannot clone builtin type: str
"""

listerrclone = """
>>> from spy.cc import clone, BuiltinTypeNotSupportedException
>>> try:
...     @clone(list)
...     class ListErrorClone:
...         pass
... except BuiltinTypeNotSupportedException as e:
...     print(e)
...
Cannot clone builtin type: list
"""

tupleerrclone = """
>>> from spy.cc import clone, BuiltinTypeNotSupportedException
>>> try:
...     @clone(tuple)
...     class ListErrorClone:
...         pass
... except BuiltinTypeNotSupportedException as e:
...     print(e)
...
Cannot clone builtin type: tuple
"""

__test__ = {
    'interrclone': interrclone,
    'strerrclone': strerrclone,
    'listerrclone': listerrclone,
    'tupleerrclone': tupleerrclone,
}


if __name__ == '__main__':
    import doctest
    doctest.testmod()
