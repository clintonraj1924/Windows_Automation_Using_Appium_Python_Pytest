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
    userName_xpath = (By.XPATH, '//*[@id="username"]')
    password_xpath = (By.XPATH, '//*[@id="password"]')
    signin_Xpath = (By.XPATH, '//*[@id="sign-in"]')
    v_name = (AppiumBy.NAME, "")
    IP_address_Or_host_Name = (AppiumBy.NAME, "IP address or hostname")
    Printer_ip_Name = (AppiumBy.NAME, "printer_ip")
    Add_using_IP_Address_name = (AppiumBy.NAME, "Add Using IP Address")
    Online_name = (AppiumBy.NAME, "Online")
    Printer_driver_installed_success = (AppiumBy.NAME, "Print driver successfully installed")
    Continue_name = (AppiumBy.NAME, "Continue")
    Printer_and_scanner = (AppiumBy.NAME, "Printers & Scanners")
    Close_Setting = (AppiumBy.NAME, "Close Settings")
    Firmware_update = (AppiumBy.NAME, "Firmware Update Available")
    No_Name = (AppiumBy.NAME, "No")
    i_frame_ID = "tag-manager"


