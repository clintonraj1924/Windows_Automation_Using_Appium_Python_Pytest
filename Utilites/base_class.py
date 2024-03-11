import time
import json
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilites.exception_handling import *


def get_data_from_inputs(key_data):
    file_path = 'Utilites\\commonData.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data[key_data]


class Base_Class:
    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.wait_50 = WebDriverWait(self.driver, 50)
        self.wait_90 = WebDriverWait(self.driver, 90)

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
        # self.wait_90.until((EC.visibility_of_element_located(by_locator)))
        self.wait_90.until(EC.presence_of_element_located(by_locator))

    def alert(self):
        try:
            alert = self.wait.until(expected_conditions.alert_is_present())
            time.sleep(2)
            alert.accept()
        except:
            print("Error: Save button not clickable")
            self.driver.save_screenshot(".\\Screen_Shots\\" + "timesheet_alert_not_working.png")

    # self.driver.save_screenshot(".\\Screen_Shots\\" + "test_login_page.png")
    def screenShort(self, image_name_png):
        self.driver.save_screenshot(".\\Screen_Shots\\" + image_name_png)

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

    def click_me(self, locator):
        self.log_my_keyword_name_and_arguments()
        element = self.get_web_element(locator)
        clicked = False
        try:
            element.click()
            clicked = True
            self.logger.logger.info(f"element clicked using selenium")
        except Exception:
            self.logger.logger.info(f"Click using WebDriver is failed")
        if not clicked:
            try:
                javascript_code = """
                function clickElement(element) {
                        if (element) {
                            element.click();
                            return true;
                        } else {
                            return false;
                        }
                    }
                return clickElement(arguments[0]);
                """
                clicked = self.driver.execute_script(javascript_code, element)
                self.logger.logger.info(f"element clicked using java script query")
                self.logger.logger.info(clicked)
            except Exception as e:
                self.logger.logger.info(f"Click using JavaScript failed")
        if not clicked:
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()
                clicked = True
                self.logger.logger.info(f"element clicked using action chains")
            except Exception:
                self.logger.logger.info(f"Click using ActionChains failed")
        if not clicked:
            message = f"Element is not clicked ==> {str(locator)}"
            self.logger.logger.info(message)
            raise ElementNotClicked(message)

    def click_using_text(self, text):
        self.log_my_keyword_name_and_arguments()
        if self.element_displayed((By.XPATH, "//*[text()='{}']".format(text))):
            self.logger.logger.info("Element clicked using text value presents in the object")
            locator = (By.XPATH, "//*[text()='{}']".format(text))
        else:
            self.logger.logger.info("Element clicked using value attribute presents in the object")
            locator = (By.XPATH, "//*[@value='{}']".format(text))
        self.click_me(locator)
