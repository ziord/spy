"""
:copyright: Copyright (c) 2020 Jeremiah Ikosin (@ziord)
:license: MIT, see LICENSE for more details
"""

import unittest
from tests.classes import *


class TestSpy(unittest.TestCase):

    def test_instance(self):
        clone1 = BaseClone()
        clone2 = DerivedClone('dev')
        self.assertTrue(isinstance(clone1, BaseClone), True)
        self.assertTrue(isinstance(clone2, DerivedClone), True)
        self.assertFalse(isinstance(clone1, Base), True)
        self.assertFalse(isinstance(clone2, Derived), True)

    def test_attributes(self):
        board_clone = BoardClone('Test', '12345678')
        base_clone = BaseClone()
        der_clone = DerivedClone('dev', 1, 2, 3)
        self.assertEqual(board_clone.name, 'Test')
        self.assertEqual(board_clone.uid, '12345678')
        self.assertListEqual(base_clone.priv(), ['_x', '_Base__y'])
        self.assertEqual(base_clone.y, 2)
        self.assertEqual(der_clone.bar(), "Base-- bar")
        self.assertTupleEqual(der_clone.args, (1, 2, 3))

    def test_class_hierarchy(self):
        self.assertTupleEqual(DerivedClone.__bases__, Derived.__bases__)

    def test_hierarchy_attributes(self):
        der_clone = DerivedClone('dev', 1, 2, 3)
        self.assertEqual(der_clone.foo(), "Base-- Foo")
        self.assertEqual(der_clone._x, 1)
        self.assertEqual(der_clone.y, 2)

    def test_slot_class(self):
        board_clone = BoardClone('Test', 12345678)
        with self.assertRaises(AttributeError):
            board_clone.stuff = "stuffy"
        self.assertEqual(str(board_clone), "BoardClone('Test', 12345678)")

    def test_name_mangling(self):
        self.assertIn('_BoardClone__xy', BoardClone.__dict__)

    def test_staticmethod(self):
        base_clone = BaseClone()
        self.assertEqual(base_clone.counter(2), '--- counting ------ counting ---')

    def test_classmethod(self):
        der_clone = DerivedClone('dev')
        der_clone.fun(6)
        self.assertEqual(DerivedClone.fun_count, 6)

    def test_property(self):
        board_clone = BoardClone()
        board = Board()
        board.name = 'foo'
        self.assertEqual(board_clone.name, 'bar')
        board_clone.name = 'foo' + board_clone.name
        self.assertEqual(board_clone.name, 'foobar')
        del board.name
        self.assertEqual(board_clone.name, 'foobar')

    def test_descriptor_client(self):
        fun_clone = FunClone()
        self.assertEqual(fun_clone.foo, 1)
        fun_clone.foo = 4
        self.assertEqual(fun_clone.foo, 4)
        self.assertTrue(hasattr(fun_clone, '_val'), True)

    def test_derived_descriptor_client(self):
        funsub_clone = FunSubClone()
        self.assertEqual(funsub_clone.foo, 1)
        funsub_clone.foo = 10
        self.assertEqual(funsub_clone.foo, 10)
        self.assertTrue(hasattr(funsub_clone, '_val'), True)

    def test_identity(self):
        board_clone = BoardClone()
        board = Board()
        # as expected, immutables have the same identity until they are modified
        # in one of the classes (clone or original), this is not the case
        # for mutables
        self.assertTrue(board.name is board_clone.name, True)
        board.name += "bar"
        self.assertFalse(board.name is board_clone.name, False)
        self.assertFalse(board_clone._l is board._l, False)
        self.assertTrue(board_clone._t is board._t, True)
        board_clone._t = (2, 3)
        self.assertFalse(board_clone._t is board._t, False)
        self.assertFalse(DerivedClone.bar is Derived.bar, False)


if __name__ == '__main__':
    unittest.main()
