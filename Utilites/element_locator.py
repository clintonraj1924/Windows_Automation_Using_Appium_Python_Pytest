from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class E_Locator:
    App_Setting_Name = (AppiumBy.NAME, "App Settings")
    Manage_HP_Account_Name = (AppiumBy.NAME, "Manage HP Account")
    Sign_In_Name = (AppiumBy.NAME, "Sign in")
    Sign_Out_Name = (AppiumBy.NAME, "Sign Out")
    Back_arrow_ID = (AppiumBy.ID, "BackArrow")
    Title_Hamburger_Button = (AppiumBy.NAME, "Menu")
    Add_Printer = (AppiumBy.NAME, "Add Printer")
    Accept_All = (AppiumBy.NAME, "Accept All")
    Next = (AppiumBy.NAME, "Next")
    Next_xpath = (By.XPATH, '//*[@id="user-name-form-submit"]')

