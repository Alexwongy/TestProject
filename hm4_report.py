import unittest


from htmltestreport import HTMLTestReport

from test_data import TestAdd

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestAdd))

runner = HTMLTestReport('test_add_report.html', '加法测试')
runner.run(suite)

# 这只是一个测试语句
