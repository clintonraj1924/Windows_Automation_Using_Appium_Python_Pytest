import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Class:
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.wait_50 = WebDriverWait(self.driver, 20)
        self.wait_90 = WebDriverWait(self.driver, 20)

    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def i_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def send_keys(self, by_locator, value):
        self.wait.until((EC.presence_of_element_located(by_locator))).send_keys(value)

    def send_keys_xl_related(self, by_locator, value):
        self.wait.until((EC.visibility_of_element_located(by_locator))).clear()
        self.wait.until((EC.visibility_of_element_located(by_locator))).send_keys(value)

    def get_text(self, by_locator):
        return self.wait.until((EC.visibility_of_element_located(by_locator))).get_attribute("innerText")

    def wait_for_Property(self, by_locator):
        self.wait_50.until((EC.visibility_of_element_located(by_locator)))

    def alert(self):
        try:
            alert = self.wait.until(expected_conditions.alert_is_present())
            time.sleep(2)
            alert.accept()
        except:
            print("Error: Save button not clickable")
            self.driver.save_screenshot(".\\Screen_Shots\\" + "timesheet_alert_not_working.png")

    # self.driver.save_screenshot(".\\Screen_Shots\\" + "test_loginpage.png")
    def screenShort(self, image_name_png):
        self.driver.save_screenshot(".\\Screen_Shots\\" + (image_name_png))

    def isClickable(self, by_locator):
        return self.wait.until(EC.element_to_be_clickable(by_locator))

    def isClickable_2(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.ID, by_locator)))
            return element
        except:
            return None

    def clear(self, by_locator):
        self.wait.until((EC.visibility_of_element_located(by_locator))).clear()
