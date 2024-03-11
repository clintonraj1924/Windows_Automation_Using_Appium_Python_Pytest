import time

from pynput.keyboard import Key, Controller

from Utilites.base_class import get_data_from_inputs
from Utilites.element_locator import E_Locator
from Utilites.exception_handling import *

keyboard = Controller()
from Utilites.base_class import Base_Class


class HP_Smart_Test(Base_Class):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def hp_smart_signin(self):
    #     self.wait_for_Property(E_Locator.App_Setting_Name)
    #     print("HP Smart Home Screen is present")
    #     self.wait_for_Property(E_Locator.Manage_HP_Account_Name)
    #     self.click(E_Locator.Manage_HP_Account_Name)
    def signin(self):
        try:
            self.wait_for_Property(E_Locator.App_Setting_Name)
            print("HP Smart Home Screen is present")
            self.wait_for_Property(E_Locator.Manage_HP_Account_Name)
            self.click(E_Locator.Manage_HP_Account_Name)  # <----------
            self.click(E_Locator.Sign_In_Name)
            time.sleep(30)
            keyboard.press(Key.esc)
            time.sleep(2)
            # keyboard.press(Key.tab)
            # clearinput()
            # keyboard.type(data_variables["email_address"])
            keyboard.type(get_data_from_inputs("email_address"))
            time.sleep(2)
            keyboard.press(Key.tab)
            try:
                # time.sleep(2)
                # keyboard.press(Key.tab)
                # time.sleep(2)
                # self.wait_for_Property(E_Locator.Next)
                # self.click(E_Locator.Next)
                self.wait_for_Property(E_Locator.Next_xpath)
                self.click(E_Locator.Next_xpath)
                # click_element("Next", AppiumBy.NAME, 50)
                print("After-next2")
            except Exception as e:
                # keyboard.press(Key.tab)
                # time.sleep(2)
                keyboard.press(Key.tab)
                time.sleep(2)
                keyboard.press(Key.enter)
            time.sleep(3)
            # keyboard.type(data_variables["email_password"])
            keyboard.type(get_data_from_inputs("email_password"))
            keyboard.press(Key.enter)
            time.sleep(15)
            keyboard.press(Key.left)
            time.sleep(2)
            keyboard.press(Key.enter)
            self.wait_for_Property(E_Locator.App_Setting_Name)
        except Exception as e:
            assert False

    def welcome_page(self):
        # Wait Accept All Button Welcome to HP Smart App Page
        try:
            self.wait_for_Property(E_Locator.Accept_All)
            self.click(E_Locator.Accept_All)
            print("HP Smart App launched Successfully!")
        except Exception as e:
            print("Failed to launch HP Smart App!")
            assert False

    def hp_smart_sign_out(self):
        try:
            self.wait_for_Property(E_Locator.App_Setting_Name)
            self.click(E_Locator.App_Setting_Name)
            if self.wait_for_Property(E_Locator.Sign_Out_Name):
                self.click(E_Locator.Sign_Out_Name)
                time.sleep(10)
            self.click(E_Locator.Back_arrow_ID)
        except Exception as ee:
            message = f"Element is not clicked ==> {str(E_Locator)}"
            raise ElementNotClicked(message)

    def HP_Smart_Menu_Add_Printer_Page(self):
        try:
            self.wait_for_Property(E_Locator.Add_Printer)
            self.click(E_Locator.Add_Printer)
        except Exception as ee:
            message = f"Element is not clicked ==> {str(E_Locator)}"
            raise ElementNotClicked(message)
