"""
:copyright: Copyright (c) 2020 Jeremiah Ikosin (@ziord)
:license: MIT, see LICENSE for more details
"""

import types
from functools import update_wrapper

__all__ = ('clone',)


def _dcopy_fn(func):
    attrs = (
        func.__code__, func.__globals__,
        func.__name__, func.__defaults__,
        func.__closure__
    )
    WRAPPER_ASSIGNMENTS = (
        '__module__',
        '__name__',
        '__qualname__',
        '__doc__',
        '__annotations__',
        '__kwdefaults__',
    )
    new_f = types.FunctionType(*attrs)
    new_f = update_wrapper(new_f, func, assigned=WRAPPER_ASSIGNMENTS)
    return new_f


def _isfinstance(func):
    watch = ('function', 'method',)
    return any(type(_).__name__ in watch for _ in (func,))


def _update_qname(func, old, new):
    name = func.__qualname__
    func.__qualname__ = name.replace(old, new) \
        if old in name else name


def clone(o_klass):
    def __clone(c_klass):
        attrs = {}
        name = c_klass.__name__
        bases = o_klass.__bases__
        slot_attrs = None
        _N_A = '__slots__', '__dict__'
        n_attr, _ev_attr = None, None
        if hasattr(o_klass, _N_A[0]):
            slot_attrs = o_klass.__slots__
        for attr in o_klass.__dict__:
            if attr == _N_A[1]:
                continue
            _attr = o_klass.__dict__.get(attr)
            o_name, n_name = o_klass.__name__, c_klass.__name__
            if hasattr(attr, '__class__'):
                _ev_attr = o_klass.__dict__.get(attr)
            if '__' in attr and attr.startswith('_' + o_name):
                n_attr = attr.replace(o_name, n_name)
            if isinstance(_attr, staticmethod):
                # noinspection PyTypeChecker
                f = _dcopy_fn(_attr.__func__)
                # noinspection PyTypeChecker
                _update_qname(f, o_name, n_name)
                attrs[attr] = staticmethod(f)
            elif isinstance(_attr, classmethod):
                # noinspection PyTypeChecker
                func = _dcopy_fn(_attr.__func__)
                # noinspection PyTypeChecker
                _update_qname(func, o_name, n_name)
                attrs[attr] = classmethod(func)
            elif _isfinstance(_attr):
                func = getattr(o_klass, attr)
                f = _dcopy_fn(func)
                _update_qname(f, o_name, n_name)
                attrs[attr] = f
            elif slot_attrs and attr not in slot_attrs:
                attrs[n_attr or attr] = _ev_attr or getattr(o_klass, attr)
            elif not slot_attrs:
                attrs[n_attr or attr] = _ev_attr or getattr(o_klass, attr)
            n_attr, _ev_attr = None, None
        del c_klass
        return type(name, bases, attrs)
    return __clone
