from Page_Object.common_utils import HP_Smart_Test
from Page_Object.basic_actions import *


class Test_Onboarding_HP_Smart:

    def test_onboarding_app(self, setup):
        self.driver = setup

        # calling page object/test login page.py
        self.comUti = HP_Smart_Test(self.driver)
        # uninstall_app(get_data_from_json("app_name"))
        self.comUti.welcome_page()
        self.comUti.signin()
        self.comUti.add_printer()
        # self.comUti.install_driver()
        # self.comUti.hp_smart_sign_out()
        # install_app_store(get_data_from_json("app_id"))


