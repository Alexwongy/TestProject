import unittest


suite = unittest.TestLoader().discover('case', 'test*.py' )#注意文件名要保持统一

unittest.TextTestRunner().run(suite)