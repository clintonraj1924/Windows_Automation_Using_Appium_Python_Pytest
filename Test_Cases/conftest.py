from datetime import time
from typing import Dict, Any

from appium.options.common import AppiumOptions
from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    #global driver

    cap: Dict[str, Any] = {
        'platformName': 'Windows',
        'app': 'AD2F1837.HPPrinterControl_v10z8vjag6ke6!AD2F1837.HPPrinterControl'
    }
    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    time.sleep(2)
    driver.quit()
    return driver


def pytest_addoption(parser):  # this will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'HP Smart'
    config._metadata['Module Name'] = 'Windows Automation'
    config._metadata['Tester'] = 'Clinton Raj'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
