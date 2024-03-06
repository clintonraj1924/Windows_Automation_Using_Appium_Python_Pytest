# run appium in CMD --> appium -p 4723
# Appium Server

from typing import Dict, Any
import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def setup_function(function):
    # global appium_Service  # connect to the appium server without open Appium GUI
    # appium_Service= AppiumService()
    # appium_Service.start()

    global driver
    cap: Dict[str, Any] = {
        'platformName': 'Windows',
        'app': 'AD2F1837.HPPrinterControl_v10z8vjag6ke6!AD2F1837.HPPrinterControl'
    }
    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(10)

    if WebDriverWait(driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "App Settings"))):
        print("HP Smart Home Screen is present")
        # driver.find_element(AppiumBy.NAME, "App Settings").click()
        # WebDriverWait(driver, 50).until(EC.presence_of_element_located((AppiumBy.NAME, "Sign Out")))
        # driver.find_element(AppiumBy.ID, "BackArrow").click()
        WebDriverWait(driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "Manage HP Account")))
        driver.find_element(AppiumBy.NAME, "Manage HP Account").click()
        WebDriverWait(driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "Sign In")))
        driver.find_element(AppiumBy.ID, "Sign In").click()


    # def signin_HP_Smart(function):
    #     if WebDriverWait(driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "App Settings"))):
    #         print("HP Smart Home Screen is present")
    #         driver.find_element(AppiumBy.NAME, "App Settings").click()
    #         if not WebDriverWait(driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "Sign Out"))):
    #             driver.find_element(AppiumBy.ID, "BackArrow").click()
    #             WebDriverWait(driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "Manage HP Account")))
    #             driver.find_element(AppiumBy.ID, "Manage HP Account").click()
    #             WebDriverWait(driver, 90).until(EC.presence_of_element_located((AppiumBy.NAME, "Sign In")))
    #             driver.find_element(AppiumBy.ID, "Sign In").click()

    else:
        print("HP Smart home screen is not present")


def tear_down(function):
    driver.quit()
    # appium_Service.stop()  # connect to the appium server without open Appium GUI

def test_demo():
    print("pass")