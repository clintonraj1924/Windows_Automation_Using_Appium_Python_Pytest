from Page_Object.common_utils import HP_Smart_Test
from Page_Object.basic_actions import *


class Test_Onboarding_HP_Smart:

    def test_onboarding_app(self, setup):
        self.driver = setup

        # calling page object/test login page.py
        self.comUti = HP_Smart_Test(self.driver)
        # self.comUti.welcome_page()
        self.comUti.signin()
        # self.comUti.add_printer()
        # self.comUti.hp_smart_sign_out()
        # self.basAct.remove_printer_driver_settings()
        # self.basAct.uninstall_app()
        # self.basAct.install_app_store()
        # uninstall_app(get_data_from_inputs("app_name"))
        # install_app_store(get_data_from_inputs("app_id"))


