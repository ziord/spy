"""
:copyright: Copyright (c) 2020 Jeremiah Ikosin (@ziord)
:license: MIT, see LICENSE for more details
"""

import unittest
import doctest
from tests import test_errors
from tests.test_features import TestSpy

suite = unittest.TestSuite()
suite.addTests((unittest.makeSuite(TestSpy),
               doctest.DocTestSuite(test_errors)))
unittest.TextTestRunner(verbosity=2).run(suite)
