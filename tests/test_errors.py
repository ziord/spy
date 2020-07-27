from spy.cc import clone

interrclone = """
>>> @clone(int)
... class IntErrorClone:
...     pass
Traceback (most recent call last):
...
spy.cc.BuiltinTypeNotSupportedException: Cannot clone builtin type: int
"""

listerrclone = """
>>> @clone(str)
... class ListErrorClone:
...     pass
Traceback (most recent call last):
...
spy.cc.BuiltinTypeNotSupportedException: Cannot clone builtin type: list
"""

__test__ = {
    'interrclone': interrclone,
    'listerrclone': listerrclone
}
