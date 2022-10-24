import unittest

from hm4_assertEqual import TestAssert

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestAssert))
unittest.TextTestRunner().run(suite)