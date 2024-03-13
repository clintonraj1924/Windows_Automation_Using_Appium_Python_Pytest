import inspect
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Page_Object.basic_actions import *
# from Utilites.pytest_logger import SingletonLogger


class Base_Class:
    def __init__(self, driver):

        self.driver = driver
        # self.logger = SingletonLogger()
        # self.logger.logger.info("Basic actions class is initiated with browser driver value")
        self.wait = WebDriverWait(self.driver, 20)
        self.wait_50 = WebDriverWait(self.driver, 50)
        self.wait_90 = WebDriverWait(self.driver, 90)
        self.basic_wait_time = WebDriverWait(self.driver, 45)

    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def click_element(self, by_element, timeout):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_element)).click()
        # self.driver.find_element(by_element).click()

    def i_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def send_keys(self, by_locator, value):
        self.wait.until((EC.presence_of_element_located(by_locator))).send_keys(value)

    def send_keys_json(self, by_locator, data_key):
        self.wait.until((EC.presence_of_element_located(by_locator))).send_keys(get_data_from_json(data_key))

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
        try:
            self.wait.until((EC.visibility_of_element_located(by_locator))).clear()
        except Exception as ee:
            pass

    def wait_for_object(self, locator, timeout=None):
        # self.log_my_keyword_name_and_arguments()
        if timeout is None:
            timeout = self.basic_wait_time
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_web_element(self, locator):
        # self.log_my_keyword_name_and_arguments()
        element = self.driver.find_element(locator[0], locator[1])
        return element

    '''def log_my_keyword_name_and_arguments(self):
        """ This function is used to collect the variable name and arguments to log in logging """
        """ To get function name """
        current_frame = inspect.currentframe()
        calling_frame = current_frame.f_back
        function_name = calling_frame.f_code.co_name
        """ To get variables in dict format """
        frame = inspect.currentframe().f_back
        format_args = ""
        for key, value in frame.f_locals.items():
            if key != "self":
                format_args += str(key) + "=" + str(value) + " "
        format_args = "No arguments" if format_args == "" else format_args
        self.logger.logger.info(f"{function_name} called   Arguments=====>: {format_args}")'''

    '''def click_me(self, locator):
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
            raise ElementNotClicked(message)'''

    '''def click_using_text(self, text):
        # self.log_my_keyword_name_and_arguments()
        if self.element_displayed((By.XPATH, "//*[text()='{}']".format(text))):
            self.logger.logger.info("Element clicked using text value presents in the object")
            locator = (By.XPATH, "//*[text()='{}']".format(text))
        else:
            self.logger.logger.info("Element clicked using value attribute presents in the object")
            locator = (By.XPATH, "//*[@value='{}']".format(text))
        # self.click_me(locator)
        self.click(locator)'''

    '''def element_displayed(self, locator, timeout=None):
        # self.log_my_keyword_name_and_arguments()
        if timeout is None:
            timeout = self.basic_wait_time
        try:
            self.wait_for_object(locator, timeout)
            return self.driver.find_element(locator[0], locator[1]).is_displayed()
        except Exception as err:
            try:
                self.scroll_element_into_view(locator)
                return self.driver.find_element(locator[0], locator[1]).is_displayed()
            except Exception as err:
                self.logger.logger.info(str(err))
                print(str(err))
                self.logger.logger.debug(
                    f"element_displayed called \n locator: {locator} > locator not available in the web page")
                return False'''

    '''def scroll_element_into_view(self, locator):
        # self.log_my_keyword_name_and_arguments()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_web_element(locator))'''

    '''def select_default_frame(self):
        self.log_my_keyword_name_and_arguments()
        self.driver.switch_to.default_content()

    def select_frame(self, locator):
        self.log_my_keyword_name_and_arguments()
        frame_element = self.get_web_element(locator)
        self.driver.switch_to.frame(frame_element)

    def back_to_body_from_frame(self):
        self.driver.switch_to.default_content()



    def is_alert_appear(self):
        self.log_my_keyword_name_and_arguments()
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.logger.logger.info(f"Alert appear")
            return True
        except:
            self.logger.logger.info(f"Alert not appear")
            return False

    def get_alert_text(self):
        self.log_my_keyword_name_and_arguments()
        if self.is_alert_appear():
            alert = self.driver.switch_to.alert
            self.logger.logger.info(f"collected alert text value:  {alert.text}")
            return alert.text
        else:
            self.logger.logger.info("Alert is not appear to get the text")
            raise AssertionError'''

    def find_element(self, by_locator):
        element = self.find_element(by_locator)
        return element



