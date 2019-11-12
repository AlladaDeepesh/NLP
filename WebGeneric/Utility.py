dynamicXpath = "//div[text()='" + data + "']/parent::*"
                    lastTag = ""
                    while not (lastTag==("td")):
                        previousParentTag = driver.find_element_by_xpath((dynamicXpath)).tag_name
                        #dynamicXpath = dynamicXpath.replace(dynamicXpath.substring(dynamicXpath.lastIndexOf(":") + 1),previousParentTag)
                        dynamicXpath = (dynamicXpath[0:int(dynamicXpath.rfind(':') + 1)]) + previousParentTag
                        #lastTag = dynamicXpath.substring(dynamicXpath.lastIndexOf(':') + 1, dynamicXpath.length())
                        lastTag = dynamicXpath[(dynamicXpath.rfind(':') + 1):dynamicXpath.__len__()]
                        dynamicXpath = dynamicXpath + "/parent::*"

# NameRadioButton = dynamicXpath[0:dynamicXpath.rfind('/')] + "//following-sibling::span[text()= 'Yes']"
# # RadioButton=NameRadioButton+"//preceeding-sibling::
# #                     driver.find_element_by_xpath(str(selectButton)).click()
if value='Yes':
    driver.find_element_by_xpath(dynamicXpath[0:dynamicXpath.rfind('/')] +"//following-sibling::input[@value='true']").click()
else:
    driver.find_element_by_xpath(dynamicXpath[0:dynamicXpath.rfind('/')] + "//following-sibling::input[@value='false']").click()