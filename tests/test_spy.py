import unittest, doctest
from tests import test_errors
from tests.test_features import TestSpy

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSpy))
suite.addTest(doctest.DocTestSuite(test_errors))
unittest.TextTestRunner(verbosity=2).run(suite)
