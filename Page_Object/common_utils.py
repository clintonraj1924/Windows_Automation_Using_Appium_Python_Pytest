import pytest
from appium.webdriver.common.appiumby import AppiumBy
from Utilites.base_class import Base_Class
from Utilites.element_locator import E_Locator


# @pytest.mark.usefixtures("setup")
class Login_Test(Base_Class):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_hp_smart_signin(self):
        # self.wait_90.until(EC.presence_of_element_located((AppiumBy.NAME, "App Settings")))
        # self.driver.find_element(AppiumBy.NAME, "Manage HP Account").click()
        self.wait_for_Property(E_Locator.App_Setting_Name)
        print("HP Smart Home Screen is present")
        self.wait_for_Property(E_Locator.Manage_HP_Account_Name)
        self.click(E_Locator.Manage_HP_Account_Name)
