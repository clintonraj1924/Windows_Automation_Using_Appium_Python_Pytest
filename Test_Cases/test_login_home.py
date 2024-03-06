import time
from typing import Dict, Any

from appium.options.common import AppiumOptions
from appium.webdriver import webdriver

from Page_Object.login_page_2 import Login_002_Test
from Utilites.readProperteFile import Read_Congig


class Test_Login_Home:
    baseURL = Read_Congig.getApplicationURL()
    userName = Read_Congig.getUserName()
    password = Read_Congig.getPassword()

    def test_login_page(self, setup):
        self.driver = setup
        cap: Dict[str, Any] = {
            'platformName': 'Windows',
            'app': 'AD2F1837.HPPrinterControl_v10z8vjag6ke6!AD2F1837.HPPrinterControl'
        }
        url = 'http://127.0.0.1:4723/wd/hub'
        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        driver.implicitly_wait(30)

        # def test_login(self, userName, password):
        self.ls = Login_002_Test(self.driver)
        self.ls.test_login(self.userName, self.password)



