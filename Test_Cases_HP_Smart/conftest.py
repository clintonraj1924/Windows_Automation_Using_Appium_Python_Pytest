import time
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from typing import Dict, Any


@pytest.fixture()
def setup(request):
    cap: Dict[str, Any] = {
        'platformName': 'Windows',
        'app': 'AD2F1837.HPPrinterControl_v10z8vjag6ke6!AD2F1837.HPPrinterControl'
    }
    url = 'http://127.0.0.1:4723/wd/hub'
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(30)
    driver.maximize_window()
    time.sleep(30)
    request.cls.driver = driver

    # yield
    # driver.quit()
    return driver
