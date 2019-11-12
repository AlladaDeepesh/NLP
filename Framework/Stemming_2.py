# from testcases import TestRegression
from Driver_2 import Driver
from test import Regression
import time
import unittest
from selenium import webdriver
from ExtentHTMLTestRunner import HTMLTestRunner
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import pandas
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Stemming():
    CaptureDict = {}
    test=''
    identifier=''
    tcName=''



    # def __init__(self):
    #     global suite
    #     global result

        # suite = unittest.TestSuite()
        # result = unittest.TestResult()
        # suite.addTest(unittest.makeSuite(Stemming))

    def ReadTC(self):
        global tcName
        global testcases
        testcases=[]

        dataframe = pandas.read_excel('../TestCases/PandasDataset.xlsx')
        Filtered_df = dataframe.drop_duplicates(['TC_NAME'])
        for Step in range(Filtered_df.__len__()):
            TC_Name = Filtered_df.iloc[Step, 0]
            testcases.append(str(TC_Name))

        for tc in range(testcases.__len__()):
            # Initiating WebDriver
            global driver
            #driver = Driver.DriverInitiation()
            global wait
            driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
            driver.implicitly_wait(15)
            # time.sleep(5)
            driver.maximize_window()
            # driver.get("https://gwdev.eyiaas.com/pc/PolicyCenter.do")
            driver.get("http://acasemdtesap01.eydev.net:8080/pc/PolicyCenter.do")

            wait = WebDriverWait(driver, 5)

            suite = unittest.TestSuite()
            result = unittest.TestResult()
            suite.addTest(unittest.makeSuite(Regression))
            # suite = unittest.TestSuite()
            # result = unittest.TestResult()
            # suite.addTest(unittest.makeSuite(Stemming))
            runner = unittest.TextTestRunner()
            print(runner.run(suite))



            dataframe = pandas.read_excel('../TestCases/PandasDataset.xlsx')
            tcName=testcases[tc]
            dataframe=dataframe.query('TC_NAME==@tcName')
            TestCaseDetails = (dataframe[['TC_DESC']])
            item = 0

            for Step in range(TestCaseDetails.__len__()):
                len = TestCaseDetails.__len__()
                #print (Step)
                global PageName
                PageName=dataframe.iloc[Step, 2]
                #print (PageName)
                Step_Desc= TestCaseDetails.iloc[item,0]
                nstr = re.sub(r'[$|.|!|=|"]',r'',Step_Desc)
                #print nstr
                # here we are telling nltk to filter all stopwords in english
                stop_words=set(stopwords.words("english"))
                #stop_words.add('Login')
                new_stopwords = set(stopwords.words('english')) - {'the'}
                # code to remove stopwords from our sentance
                # creating an empty list
                global filtered_Sentence
                filtered_Sentence = []
                New_Filtered_Sentence=[]
                New_filtered_Sentence=[]
                words=word_tokenize(nstr)
                for w in words:
                    if w not in new_stopwords:
                        filtered_Sentence.append(w)
                #print filtered_Sentencedifference
                counter=0
                loop_iter=1
                for each_word in filtered_Sentence:
                    if each_word.find("'")==0:
                        counter=counter+1
                loop_counter=counter/2
                for loop_iter in range(loop_counter):
                    pos_word=0
                    found_flag=False
                    added_flag = False
                    filter_index=0
                    word_pos=-1
                    for each_word in filtered_Sentence:
                        word_pos=word_pos+1
                        pos_word = pos_word + 1
                        if ((filtered_Sentence[word_pos].find("'") == 0) and (found_flag == True)):
                            end_word = pos_word - 1
                            difference = end_word - start_word
                            if difference == 1:
                                keyword = filtered_Sentence[start_word] + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                # end word is again startword for next popup element
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.insert(start_word, keyword)
                                word_pos=word_pos-2
                                found_flag = False
                                break
                            elif difference == 2:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.insert(start_word, keyword)
                                word_pos = word_pos - 3
                                found_flag = False
                                break
                            elif difference == 3:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.insert(start_word, keyword)
                                word_pos = word_pos - 4
                                found_flag = False
                                break
                            elif difference == 4:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.insert(start_word, keyword)
                                word_pos = word_pos - 5
                                found_flag = False
                                break
                            elif difference == 5:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' +  filtered_Sentence[start_word + 4] +' ' + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.insert(start_word, keyword)
                                word_pos = word_pos - 6
                                found_flag = False
                                break
                            elif difference == 6:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' +  filtered_Sentence[start_word + 4] +' '  +  filtered_Sentence[start_word + 5] +' '  + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                word_pos = word_pos - 7
                                filtered_Sentence.insert(start_word, keyword)
                                found_flag = False
                                break
                            elif difference == 7:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' +  filtered_Sentence[start_word + 4] +' '  +  filtered_Sentence[start_word + 5] +' '  +  filtered_Sentence[start_word + 6] +' '  + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                word_pos = word_pos - 8
                                filtered_Sentence.insert(start_word, keyword)
                                found_flag = False
                                break
                            elif difference == 8:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' +  filtered_Sentence[start_word + 4] +' '  +  filtered_Sentence[start_word + 5] +' '  +  filtered_Sentence[start_word + 6] +' '  +  filtered_Sentence[start_word + 7] +' '  + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                word_pos = word_pos - 9
                                filtered_Sentence.insert(start_word, keyword)
                                found_flag = False
                                break
                            elif difference == 9:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' +  filtered_Sentence[start_word + 4] +' '  +  filtered_Sentence[start_word + 5] +' '  +  filtered_Sentence[start_word + 6] +' '  +  filtered_Sentence[start_word + 7] +' '  +  filtered_Sentence[start_word + 8] +' '  + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                word_pos = word_pos - 10
                                filtered_Sentence.insert(start_word, keyword)
                                found_flag = False
                                break
                            elif difference == 10:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' +  filtered_Sentence[start_word + 4] +' '  +  filtered_Sentence[start_word + 5] +' '  +  filtered_Sentence[start_word + 6] +' '  +  filtered_Sentence[start_word + 7] +' '  +  filtered_Sentence[start_word + 8] +' '  +  filtered_Sentence[start_word + 9] +' '  + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                word_pos = word_pos - 11
                                filtered_Sentence.insert(start_word, keyword)
                                found_flag = False
                                break
                            elif difference == 11:
                                keyword = filtered_Sentence[start_word] + ' ' + filtered_Sentence[start_word + 1] + ' ' + filtered_Sentence[start_word + 2] + ' ' + filtered_Sentence[start_word + 3] + ' ' +  filtered_Sentence[start_word + 4] +' '  +  filtered_Sentence[start_word + 5] +' '  +  filtered_Sentence[start_word + 6] +' '  +  filtered_Sentence[start_word + 7] +' '  +  filtered_Sentence[start_word + 8] +' '  +  filtered_Sentence[start_word + 9] +' '  +  filtered_Sentence[start_word + 10] +' '  + filtered_Sentence[end_word]
                                keyword = keyword.replace("'", "")
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                filtered_Sentence.pop(start_word)
                                word_pos = word_pos - 12
                                filtered_Sentence.insert(start_word, keyword)
                                found_flag = False
                                break
                        elif (filtered_Sentence[word_pos].find("'") == 0):
                            found_flag = True
                            start_word = pos_word - 1

                print (filtered_Sentence, PageName)

                #test_01 = StemObj.create_a_function()



                # suite.addTest(unittest.makeSuite(tcName))
                # runner = unittest.TextTestRunner()
                # print(runner.run(suite))
                fp = open("report.html", 'wb')
                runner = HTMLTestRunner(stream=fp,
                                        title='test report_Deepesh',
                                        description='test report detail Deepesh 123:')
                runResult = runner.run(suite)
                # StemObj.Execution(filtered_Sentence,PageName,driver,wait)
                item=item+1
                if item==len:
                    break

    # def create_a_function(*args, **kwargs):
    #     def function_template(*args, **kwargs):
    #         if "test" == 'test':
    #             print("--->")
    #
    #             assert 1 == 1
    #             print("--PASS->>>")
    #         #StemObj.Execution(filtered_Sentence, PageName, driver, wait)
    #     return function_template

    def Execution(self,filtered_Sentence,PageName,driver,wait):

        import pandas
        ObjectRepo_DF = pandas.read_excel('../ObjectRepo/ObjectRepo.csv', sheet_name=PageName)
        index = 0

        for keyword in filtered_Sentence:
            KeywordFlag = False
            # key1=keyword.replace(" ","")
            # key2=(keyword.replace(" ","")).lower()
            # key3=(keyword.replace(" ","")).upper()

            if keyword in ['capture']:
                StemObj.fnCaptureElement(filtered_Sentence,driver)
                index = index + 1
                KeywordFlag=True
            if keyword in ['WebTable'] and KeywordFlag==False:
                StemObj.fnWebTableAction(filtered_Sentence,driver)
                KeywordFlag=True
            if keyword.lower() in ['radiogroup'] and KeywordFlag==False:
                StemObj.fnRadioAction(filtered_Sentence,driver)
                KeywordFlag=True
            else:
                ClickFlag = False
                Found_Flag = False
                if KeywordFlag==False:
                    if index != (len(filtered_Sentence)):
                        if index != (len(filtered_Sentence)-1):
                            next_data = filtered_Sentence[index + 1]
                        else:
                            next_data=''
                        # keywords to ignore
                        if next_data.lower() == 'dropdown':
                            StemObj.fnclickOnDownArrowButton(keyword, driver)
                            #index=index+1
                            KeywordFlag = True

                        data=filtered_Sentence[index]
                        if data.lower() in ['capture'] and KeywordFlag==False:
                            data = filtered_Sentence[index]
                            StemObj.fnCaptureElement(data, driver)
                            KeywordFlag = True
                        if data.lower() not in ['under'] and KeywordFlag==False:
                            driver.implicitly_wait(0.1)
                            xPathToFieldBasedOnLabel = "//div[text()='" + keyword + "']//parent::div//parent::div[contains(@class,'Button')]"
                            if (driver.find_elements_by_xpath(xPathToFieldBasedOnLabel).__len__()) !=0:
                                Found_Flag = True
                                ElementType='button'
                            else:
                                xPathToFieldBasedOnLabel = "//div[text()='" + keyword + "']/following-sibling::*//input"
                                if (driver.find_elements_by_xpath(xPathToFieldBasedOnLabel).__len__()) !=0:
                                    Found_Flag = True
                                else:
                                    xPathToFieldBasedOnLabel = "//div[text()='" + keyword + "']/following-sibling::*//select"
                                    if (driver.find_elements_by_xpath(xPathToFieldBasedOnLabel).__len__()) !=0:
                                        Found_Flag = True
                                    else:
                                        xPathToFieldBasedOnLabel = "//div[text()='" + keyword + "']//parent::div//parent::div[contains(@class,'Link')]"
                                        if (driver.find_elements_by_xpath(xPathToFieldBasedOnLabel).__len__()) != 0:
                                            Found_Flag = True
                                        else:
                                            xPathToFieldBasedOnLabel = "//div[contains(@class,'gw-big-button ') and contains(@id,'" + keyword + "')]"
                                            if (driver.find_elements_by_xpath(xPathToFieldBasedOnLabel).__len__()) != 0:
                                                Found_Flag = True
                                                ElementType = 'button'
                                            else:
                                                Dropdowndata = filtered_Sentence[index-2]
                                                data=filtered_Sentence[index-3]
                                                if Dropdowndata.lower()=='dropdown':
                                                    xPathToFieldBasedOnLabel ="//div[contains(@id,'" + data + "')]//child::*[contains(text(),'" + keyword + "')]"
                                                    if (driver.find_elements_by_xpath(xPathToFieldBasedOnLabel).__len__()) != 0:
                                                        Found_Flag = True
                                                        ElementType = 'button'
                                                else:
                                                    if keyword in ['Create New Account']:
                                                        StemObj.fnIndentifyElement(keyword,driver)
                                                    else:
                                                        xPathToFieldBasedOnLabel = "//div[contains(text(),'" + keyword + "')]//parent::div[contains(@class,'gw-action--inner gw-hasDivider')]//parent::div[contains(@id,'" + StemObj.identifier + "')]"
                                                        if (driver.find_elements_by_xpath(
                                                            xPathToFieldBasedOnLabel).__len__()) != 0:
                                                            Found_Flag = True

                            if Found_Flag==True:
                                driver.implicitly_wait(15)
                                tagName = driver.find_element_by_xpath(xPathToFieldBasedOnLabel).tag_name
                                typeAtrribute = driver.find_element_by_xpath(xPathToFieldBasedOnLabel).get_attribute('type')
                                if tagName.lower() == 'input':
                                    if typeAtrribute.lower() == 'checkbox':
                                        checkBox = driver.find_element_by_xpath(xPathToFieldBasedOnLabel)
                                        checkBox.click()
                                        KeywordFlag = True
                                    elif typeAtrribute.lower() in ['text','password'] and KeywordFlag==False:
                                        if not ((filtered_Sentence.__len__() - 1) == index):
                                            #editBox = driver.findElement(By.xpath(xPathToFieldBasedOnLabel))
                                            data = filtered_Sentence[index + 1]
                                            StemObj.fnInputElement(xPathToFieldBasedOnLabel, data, driver, wait)
                                            KeywordFlag = True
                                elif tagName.lower() == 'select' and KeywordFlag==False:
                                    dropDown = driver.find_element_by_xpath(xPathToFieldBasedOnLabel)
                                    #inputElement = Select(driver.find_element_by_xpath(keyword))
                                    dropDown.select_by_visible_text(keyword + 1)
                                    KeywordFlag = True
                                elif tagName.lower() == 'div' and KeywordFlag==False and ElementType=='button':
                                    ButtonElement = driver.find_element_by_xpath(xPathToFieldBasedOnLabel)
                                    ButtonElement.click()
                                    time.sleep(2)
                        index=index+1



    def fnInputElement(self,keyword,data,driver,wait):
        NotFound = False
        try:
            #inputElement=wait.until(EC.visibility_of(driver.find_element_by_name(keyword)))
            #inputElement = driver.find_element_by_name(Element)
            inputElement = driver.find_element_by_xpath(keyword)
            inputElement.send_keys(data)
            time.sleep(1)
            assert True
            print(keyword +" is entered data as : " + data)
        except:
            NoSuchElementException

    def fnCaptureElement(self,filtered_Sentence,driver):
        NotFound = False
        index=1
        try:
            for keyword in filtered_Sentence:
                if not index==filtered_Sentence.__len__():
                    data = filtered_Sentence[index]
                    xPathToLabel = "//div[text()='" + data + "']";
                    labelValue = driver.find_element_by_xpath(xPathToLabel + "/parent::*//div[contains(@class, 'gw-vw--value gw-align-h--left')]").text;
                    StemObj.CaptureDict[data]=labelValue
                    index=index+1
                    assert True
                    print(labelValue + " data is captured sucessfully : " )
        except:
            NoSuchElementException
            index=index+1

    def fnWebTableAction(self,filtered_Sentence,driver):
        NotFound = False
        index=0
        try:
            for keyword in filtered_Sentence:
                if keyword.find('WebTable')>=0:
                    data = filtered_Sentence[index+2]
                    dynamicXpath = "//div[text()='" + data + "']/parent::*"
                    lastTag = ""
                    while not (lastTag==("tr")):
                        previousParentTag = driver.find_element_by_xpath((dynamicXpath)).tag_name
                        #dynamicXpath = dynamicXpath.replace(dynamicXpath.substring(dynamicXpath.lastIndexOf(":") + 1),previousParentTag)
                        dynamicXpath = (dynamicXpath[0:int(dynamicXpath.rfind(':') + 1)]) + previousParentTag
                        #lastTag = dynamicXpath.substring(dynamicXpath.lastIndexOf(':') + 1, dynamicXpath.length())
                        lastTag = dynamicXpath[(dynamicXpath.rfind(':') + 1):dynamicXpath.__len__()]
                        dynamicXpath = dynamicXpath + "/parent::*"

                    selectButton = dynamicXpath[0:dynamicXpath.rfind('/')] + "//div[text()='Select']"
                    driver.find_element_by_xpath(str(selectButton)).click()
                    index=index+1
                else:
                    index=index+1
        except:
            NoSuchElementException
            index = index + 1
    def fnRadioAction(self,filtered_Sentence,driver):
        NotFound = False
        index=0
        try:
            for keyword in filtered_Sentence:
                if (keyword.lower()).find('radiogroup')>=0:
                    data = filtered_Sentence[index+1]
                    value=filtered_Sentence[index+2]
                    dynamicXpath = "//div[text()='" + data + "']/parent::*"
                    lastTag = ""
                    while not (lastTag==("td")):
                        previousParentTag = driver.find_element_by_xpath((dynamicXpath)).tag_name
                        #dynamicXpath = dynamicXpath.replace(dynamicXpath.substring(dynamicXpath.lastIndexOf(":") + 1),previousParentTag)
                        dynamicXpath = (dynamicXpath[0:int(dynamicXpath.rfind(':') + 1)]) + previousParentTag
                        #lastTag = dynamicXpath.substring(dynamicXpath.lastIndexOf(':') + 1, dynamicXpath.length())
                        lastTag = dynamicXpath[(dynamicXpath.rfind(':') + 1):dynamicXpath.__len__()]
                        dynamicXpath = dynamicXpath + "/parent::*"

                    if value.lower()=='yes':
                        driver.find_element_by_xpath(dynamicXpath[0:dynamicXpath.rfind('/')] + "//following-sibling::input[@value='true']").click()
                    else:
                        driver.find_element_by_xpath(dynamicXpath[0:dynamicXpath.rfind('/')] + "//following-sibling::input[@value='false']").click()
                else:
                    index=index+1
        except:
            NoSuchElementException
            index = index + 1

    def fnSelectElement(self,Element,data,driver):
        NotFound = False
        try:
            inputElement = Select(driver.find_element_by_name(Element))
            inputElement.select_by_visible_text(data)
            time.sleep(1)
        except:
            NoSuchElementException

    def fnPerformAction(self,id,driver):
        try:
            inputElement = driver.find_element_by_id(id)
            action = ActionChains(driver)
            #action.move_to_element(inputElement).perform()
            #time.sleep(1)
            action.click(inputElement).perform()
            time.sleep(3)
            #inputElement = WebDriverWait(driver, 5).until(EC.visibility_of(inputElement))
            #inputElement.click()
        except:
            NoSuchElementException

    def fnClick(self,id,driver):
        try:

            inputElement = driver.find_element_by_id(id)
            action = ActionChains(driver)
            #action.move_to_element(inputElement).perform()
            #time.sleep(2)
            action.click(inputElement).perform()
            time.sleep(3)
            #inputElement=WebDriverWait(driver,5).until(EC.visibility_of(inputElement))
            #inputElement.click()
            #action.move_to_element(inputElement).click().build().perform()
            #inputElement.click()
            #time.sleep(8)
            assert True
            print(id + " Element is clicked " )
        except:
            NoSuchElementException
            assert False
            print(id + " Element is not clicked ")

    def fnclickOnDownArrowButton(self, keyword, driver):
        xPathToArrowButton = "//div[contains(@id,'" + keyword + "')]//child::*[contains(@class,'gw-icon gw-icon--expand')]"

        driver.find_element_by_xpath(xPathToArrowButton).click()
        time.sleep(2)

    def fnIndentifyElement(self, keyword, driver):
        if keyword == "Create New Account":
            ElementxPath = "//div[contains(@id,'NewAccountButton')]//child::div[contains(@class,'gw-action--inner') and (@data-gw-click='toggleSubMenu')]"
            StemObj.identifier='NewAccountButton'

        driver.find_element_by_xpath(ElementxPath).click()
        time.sleep(2)

class case_01_test(unittest.TestCase):
    """testcase 01"""
    def setUp(self):
        print("--->")

    def test_case_01(self):
        print("test_01")
        print("--->>>")

    def tearDown(self):
        pass





StemObj = Stemming()
StemObj.ReadTC()


