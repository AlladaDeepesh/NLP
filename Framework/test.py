
import pandas
import unittest
from ExtentHTMLTestRunner import HTMLTestRunner


class Regression(unittest.TestCase):

    def create_a_function(*args, **kwargs):

        def function_template(*args, **kwargs):
            if "test" == 'test':
                print("--->")

                assert 1 == 1
                print("--PASS->>>")

        return function_template



    test_02 = create_a_function()
    test_03 = create_a_function()

