import unittest


class TestAssert(unittest.TestCase):
    def test_equal1(self):
        self.assertEqual(10,10)

    def test_equal2(self):
        self.assertEqual(10,10)

    def test_in(self):
        self.assertIn('admin', '欢迎admin登录')