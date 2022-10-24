import unittest


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:  #方法级别的fiture
        print('2.打开网页，点击登录')
    def tearDown(self) -> None:
        print('4.关闭网页')

    @classmethod  #类级别的fixture
    def setUpClass(cls) -> None:
        print('1.打开浏览器')

    @classmethod
    def tearDownClass(cls) -> None:
        print('5.关闭浏览器')
    def test_1(self):
        print('3.输入用户名密码验证码1，点击登录（每次，测试方法）')

    def test_2(self):
        print('3.输入用户名密码验证码2，点击登录（每次，测试方法）')

    def test_3(self):
        print('3.输入用户名密码验证码3，点击登录（每次，测试方法）')