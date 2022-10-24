import unittest

from tools import add
from read_data1 import build_add_data, build_add_data_1
from parameterized import parameterized

class TestAdd(unittest.TestCase):
    @parameterized.expand(build_add_data_1)
    def test_add(self, a, b, expect):
        print(f'a:{a}, b:{b}, expect:{expect}')
        self.assertEqual(expect, add(a,b))


if __name__ == '__main__':
    unittest.main()