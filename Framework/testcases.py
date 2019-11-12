import unittest
# from Stemming_2 import Stemming
# print (Stemming.testcases)
import pandas
class TestRegression(unittest.TestCase):

    def create_a_function(*args, **kwargs):

        def function_template(*args, **kwargs):
            #StemObj.Execution(filtered_Sentence, PageName, driver, wait)
            if "test" == 'test':
                print("--->")

                assert 1 == 1
                print("--PASS->>>")

        return function_template


    test_01 = create_a_function()
    test_02 = create_a_function()
    # testcases = []
    # dataframe = pandas.read_excel('../TestCases/PandasDataset.xlsx')
    # Filtered_df = dataframe.drop_duplicates(['TC_NAME'])
    # for Step in range(Filtered_df.__len__()):
    #     TC_Name = Filtered_df.iloc[Step, 0]
    #     testcases.append(str(TC_Name))
    # for tc in range(testcases.__len__()):
    #     testcases[tc]=create_a_function()

