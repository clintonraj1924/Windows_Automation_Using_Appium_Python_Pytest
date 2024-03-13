from Page_Object.common_utils import HP_Smart_Test
from Page_Object.basic_actions import *


class Test_CleanUp_HP_Smart:
    def test_cleanup(self, setup):
        self.driver = setup

        self.comUti = HP_Smart_Test(self.driver)
        # remove printer
        # signout
        # remove printer driver
        # uninstall app
        self.comUti.remove_printer_on_Dashboard()
        self.comUti.sign_out()
        remove_printer_driver_settings("driver_name")
        uninstall_app(get_data_from_json("app_name"))
        self.comUti.close_settings_app()
