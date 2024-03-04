# run appium in CMD --> appium -p 4723
# Appium Server

from typing import Dict, Any
import time
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support import expected_conditions as EC

def setup_function(function):
    # global appium_Service  # coonect to the appium server without open Appium GUI
    # appium_Service= AppiumService()
    # appium_Service.start()

    global driver
    cap: Dict[str, Any]={
        'platformName': 'Windows',
        'app': 'AD2F1837.HPPrinterControl_v10z8vjag6ke6!AD2F1837.HPPrinterControl'
    }
    url= 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(10)

def tear_down(function):
    driver.quit()
    # appium_Service.stop()  # coonect to the appium server without open Appium GUI

def test_demo():
    print("pass")