from test import Regression
from ExtentHTMLTestRunner import HTMLTestRunner
import unittest

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(Regression))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    fp = open("report.html", 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='test report_Deepesh',
                            description='test report detail Deepesh 123:')
    runResult = runner.run(suite)
my_suite()