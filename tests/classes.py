"""
:copyright: Copyright (c) 2020 Jeremiah Ikosin (@ziord)
:license: MIT, see LICENSE for more details
"""

from spy.cc import clone, BuiltinTypeNotSupportedException


#####################################
#             ORIGINALS
#####################################

class Base:
    def __init__(self):
        self.name = 'Base'
        self._x = 1
        self.__y = 2

    def foo(self):
        return self.name + '-- Foo'

    def priv(self):
        return [x for x in self.__dict__ if x.startswith('_')]

    @staticmethod
    def counter(x):
        return '--- counting ---'*x

    @property
    def y(self):
        return self.__y


class Derived(Base):
    def __init__(self, arg, *args):
        Base.__init__(self)
        self.__z = 5
        self.arg = arg
        self.args = args

    def bar(self):
        return self.name + '-- bar'

    @classmethod
    def fun(cls, count):
        cls.fun_count = count


class Board:
    __slots__ = '_name', '_id', '_t', '_l'

    def __init__(self, name='bar', id=0):
        self._name = name
        self._id = id
        self._t = (1,)
        self._l = [3]

    _xx = 5
    __xy = 10
    xz = 15

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def uid(self):
        return self._id

    @uid.setter
    def uid(self, id_str):
        self._id = id_str

    def __str__(self):
        return self.__class__.__name__ + f"({self.name!r}, {self.uid!r})"


class Desc:
    def __init__(self):
        self.val = 1

    def __set__(self, instance, value):
        setattr(instance, '_val', value)

    def __get__(self, instance, owner):
        return instance._val if hasattr(instance, '_val') else self.val


class Fun:
    foo = Desc()


class FunSub(Fun):
    ...

#####################################
#               CLONES
#####################################


@clone(Base)
class BaseClone:
    pass


@clone(Derived)
class DerivedClone:
    pass


@clone(Board)
class BoardClone:
    pass


@clone(Fun)
class FunClone:
    ...


@clone(FunSub)
class FunSubClone:
    ...


@clone(int)
class IntErrorClone:
    pass


@clone(list)
class ListErrorClone:
    pass
