'''import logging, datetime, os


def get_parent_framework_path():  # <-----
    current_path = os.getcwd()
    get_parent = os.path.dirname(current_path)
    # In case the tests are running in the Azure pipeline agent machine
    if "Appium_Windows_Automation\\HP_Smart_Automation_Appium_Windows" not in get_parent:
        return os.path.join(current_path, 'Appium_Windows_Automation', 'HP_Smart_Automation_Appium_Windows')
    return get_parent


class SingletonLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonLogger, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            time_now = datetime.datetime.now()
            time_str = time_now.strftime("%Y_%m_%d_%H_%M_%S")
            time_str = time_str.replace(":", "_")
            test_log_path = f"\\reports\\test_logs_{time_str}.log"
            file_handler = logging.FileHandler(get_parent_framework_path() + test_log_path)
            file_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(file_handler)
        return cls._instance'''
