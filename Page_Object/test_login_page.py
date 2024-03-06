from Utilites.base_class import Base_Class
from Utilites.element_locator import E_Locator


class Login_Test(Base_Class):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_hp_smart_signin(self):
        if self.wait_for_Property(E_Locator.App_Setting_Name):
            print("HP Smart Home Screen is present")
            self.wait_for_Property(E_Locator.Manage_HP_Account_Name)
            self.click(E_Locator.Manage_HP_Account_Name)