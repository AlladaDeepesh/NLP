class Driver():

    # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    # cap = DesiredCapabilities().INTERNETEXPLORER
    # cap['browserName'] = "internet explorer"
    # cap['ignoreProtectedModeSettings'] = True
    # cap['IntroduceInstabilityByIgnoringProtectedModeSettings'] = True
    # cap['nativeEvents'] = True
    # cap['ignoreZoomSetting'] = True
    # cap['requireWindowFocus'] = True
    # cap['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
    # driver=webdriver.Ie(executable_path='../Drivers/IEDriverServer.exe')
    # def __init__(self):
    #     pass
    def DriverInitiation(self):
        from selenium import webdriver
        import time
        from selenium.webdriver.common.keys import Keys
        driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        driver.implicitly_wait(15)
        #time.sleep(5)
        driver.maximize_window()
        #driver.get("https://gwdev.eyiaas.com/pc/PolicyCenter.do")
        driver.get("http://acasemdtesap01.eydev.net:8080/pc/PolicyCenter.do")
        #time.sleep(2)
        # inputElement =driver.find_element_by_name('Login-LoginScreen-LoginDV-username')
        # inputElement.send_keys("su")
        # time.sleep(1)
        # inputElement =driver.find_element_by_name('Login-LoginScreen-LoginDV-password')
        # inputElement.send_keys("gw")
        # time.sleep(1)
        # inputElement=driver.find_element_by_id('Login-LoginScreen-LoginDV-submit')
        # inputElement.click()
        return driver
