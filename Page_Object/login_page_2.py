import time

# import openpyxl
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from Utilites import xl_utils
from Utilites.base_class import Base_Class
from Utilites.custom_logger import LogGen
from Utilites.element_locator import EL_Locator


class Login_002_Test(Base_Class):
    logger = LogGen.loggen()
    path = ".//testData/Clinton_Raj_Timesheet_Entry.xlsx"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, userName, password):
        self.logger.info("************************ Login_002_Test **************************************")
        self.logger.info("************************ login_test **************************************")

        # self.send_keys(EL_Locator.textBox_userName_ID, userName)
        # self.send_keys(EL_Locator.textBox_password_ID, password)
        # self.click(EL_Locator.login_btn_ID)
        if self.wait_for_Property(EL_Locator.App_Setting_Name):
            print("HP Smart Home Screen is present")
            self.wait_for_Property(EL_Locator.Manage_HP_Account_NAme)
            self.click(EL_Locator.Manage_HP_Account_NAme)
