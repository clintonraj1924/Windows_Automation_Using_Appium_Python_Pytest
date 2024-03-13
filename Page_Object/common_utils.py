import os
import psutil
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from pynput.keyboard import Key, Controller
from Utilites.base_class import Base_Class
from Page_Object.basic_actions import *
from Utilites.element_locator import E_Locator
from Utilites.exception_handling import *

keyboard = Controller()

# # Set the desired capability for HP Smart App
# desired_caps = {'app': "AD2F1837.HPPrinterControl_v10z8vjag6ke6!AD2F1837.HPPrinterControl",
#                 'platformName': "Windows",
#                 'platformVersion': "10", 'deviceName': "WindowsPC", "ms:experimental-webdriver": True,
#                 "ms:waitForAppLaunch": "50"}
# Set the desired capability for HP Smart App
desired_caps = {}
desired_caps['app'] = "AD2F1837.HPPrinterControl_v10z8vjag6ke6!AD2F1837.HPPrinterControl"
desired_caps['platformName'] = "Windows"
desired_caps['platformVersion'] = "10"
desired_caps['deviceName'] = "WindowsPC"
desired_caps["ms:experimental-webdriver"] = True
desired_caps["ms:waitForAppLaunch"] = "50"


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
            # self.click(E_Locator.Manage_HP_Account_Name)
            # self.click(E_Locator.Sign_In_Name)
            self.click_element(E_Locator.Manage_HP_Account_Name, 40)
            self.click_element(E_Locator.Sign_In_Name, 40)  # <-------
            time.sleep(20)
            # keyboard.press(Key.esc)
            # time.sleep(2)
            # keyboard.press(Key.tab)
            # clearinput()
            # keyboard.type(data_variables["email_address"])
            keyboard.type(get_data_from_json("email_address"))
            time.sleep(2)
            keyboard.press(Key.tab)
            try:
                # time.sleep(2)
                # keyboard.press(Key.tab)
                # time.sleep(2)
                # self.wait_for_Property(E_Locator.Next)
                # self.click(E_Locator.Next)
                self.wait_for_Property(E_Locator.Next_xpath)
                time.sleep(5)
                self.click(E_Locator.Next_xpath)
            except Exception as e:
                # keyboard.press(Key.tab)
                # time.sleep(2)
                keyboard.press(Key.tab)
                time.sleep(2)
                keyboard.press(Key.enter)
            time.sleep(3)
            # self.i_frame(E_Locator.i_frame_ID)
            # keyboard.type(data_variables["email_password"])
            keyboard.type(get_data_from_json("email_password"))
            # self.clear(E_Locator.password_xpath)
            # self.send_keys(E_Locator.password_xpath, get_data_from_inputs("email_password"))
            # self.send_keys_json(E_Locator.signin_Xpath, "email_password")
            time.sleep(1)
            keyboard.press(Key.enter)
            # self.click_element(E_Locator.signin_Xpath, 20)
            time.sleep(15)
            keyboard.press(Key.left)
            time.sleep(5)
            mouse = Controller()
            mouse.press(Key.enter)
            print("print-1")
            time.sleep(2)
            mouse_2 = Controller()
            mouse_2.pressed(Key.enter)
            time.sleep(1)
            mouse_2.release(Key.enter)
            print("print-2")
            self.wait_for_Property(E_Locator.App_Setting_Name)
            time.sleep(10)
            try:
                os.system("taskkill /im msedge.exe /f")
                print("Edge browser closed")
            except Exception as e:
                os.system("taskkill /im chrome.exe /f")
                print("Chrome browser closed")
        except Exception as e:
            self.sign_out()
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
                time.sleep(5)
                self.click_element(E_Locator.Sign_Out_Name, 20)
            # self.click(E_Locator.Back_arrow_ID)
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

    def sign_out(self):
        try:
            if self.wait_for_Property(E_Locator.v_name):
                self.click(E_Locator.v_name)
                time.sleep(5)
                self.click(E_Locator.Sign_Out_Name)
                time.sleep(1)
                self.click(E_Locator.Sign_Out_Name)
        except Exception as e:
            for proc in psutil.process_iter():
                if proc.name() == "HP.Smart.exe":
                    proc.kill()
            driver1 = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=desired_caps)  # desired_capabilities=desired_caps

            driver1.find_element(AppiumBy.NAME, "").click()
            time.sleep(5)
            elements = driver1.find_elements(AppiumBy.NAME, "Sign Out")
            elements[0].click()

            driver1.find_element(AppiumBy.NAME, "Sign Out").click()
            time.sleep(5)
        print("Logged out")
        for proc in psutil.process_iter():
            if proc.name() == "HP.Smart.exe":
                proc.kill()

    def add_printer(self):
        try:
            self.wait_for_Property(E_Locator.Add_Printer)
            self.click(E_Locator.Add_Printer)
            try:
                self.wait_for_Property(E_Locator.IP_address_Or_host_Name)
                self.click(E_Locator.IP_address_Or_host_Name)
                self.send_keys(E_Locator.IP_address_Or_host_Name, get_data_from_json("printer_ip"))
                keyboard.press(Key.enter)
                time.sleep(2)
            except Exception as e:
                self.wait_for_Property(E_Locator.Add_using_IP_Address_name)
                self.click(E_Locator.Add_using_IP_Address_name)
                print("Add Using IP Address Button Click Success")
                self.send_keys(E_Locator.IP_address_Or_host_Name, get_data_from_json("printer_ip"))
                keyboard.press(Key.enter)
                time.sleep(2)
            self.wait_for_Property(E_Locator.Online_name)
            time.sleep(10)
            self.click(E_Locator.Online_name)
        except Exception as exinfo:
            self.sign_out()
            assert False

    def install_driver(self):
        try:
            self.wait_for_Property(E_Locator.Printer_driver_installed_success)
            self.click(E_Locator.Printer_driver_installed_success)
            time.sleep(30)
            # elements = driver.find_elements(AppiumBy.NAME, "Continue")
            elements = self.find_element(E_Locator.Continue_name)
            elements[2].click()
            self.wait_for_Property(E_Locator.App_Setting_Name)
            print("Printer Onboarded Successfully on HP Smart APP!")
        except Exception as e:
            time.sleep(10)
            keyboard.press(Key.tab)
            time.sleep(2)
            keyboard.press(Key.tab)
            time.sleep(2)
            keyboard.press(Key.tab)
            time.sleep(2)
            keyboard.press(Key.tab)
            time.sleep(2)
            keyboard.press(Key.tab)
            self.wait_for_Property(E_Locator.Printer_and_scanner)
            self.click(E_Locator.Printer_and_scanner)
            time.sleep(10)
            print("Working with printer-driver flow-1")
            self.wait_for_Property(E_Locator.Close_Setting)
            self.click(E_Locator.Close_Setting)
            # Attempt to close the Settings app
            self.close_settings_app()
            time.sleep(10)
            self.wait_for_Property(E_Locator.Continue_name)
            self.click(E_Locator.Continue_name)
            self.wait_for_Property(E_Locator.App_Setting_Name)
            print("Printer Onboarded Successfully on HP Smart APP!!")
            time.sleep(3)
            try:
                self.wait_for_Property(E_Locator.Firmware_update)
                # self.click(E_Locator.No_Name)
                self.click_element(E_Locator.No_Name, 20)
            except Exception as e:
                print("Firmware Update UI does not Exist!!!")

    def close_settings_app(self):
        time.sleep(3)
        setting_menu_cmd = "Stop-Process -Name 'SystemSettings'"
        try:
            if subprocess.run(["powershell", "-Command", setting_menu_cmd]):
                print(f"Windows Setting Menu Closed successfully")
                time.sleep(2)
        except Exception as e:
            print(f"Failed to Close the Windows Setting Menu")

    def remove_printer_on_Dashboard(self):
        time.sleep(5)
        self.wait_for_Property(E_Locator.Title_Hamburger_Button)
        self.wait_for_object(E_Locator.Title_Hamburger_Button, 20)
