from Page_Object.common_utils import HP_Smart_Test
from Page_Object.basic_actions import Basic_Actions


class Test_Onboarding_HP_Smart:

    def test_onboarding_app(self, setup):
        self.driver = setup


        # calling page object/test login page.py
        self.cu = HP_Smart_Test(self.driver)
        self.bc = Basic_Actions(self.driver)
        self.cu.signin()
        self.cu.hp_smart_sign_out()
        self.bc.remove_printer_driver_settings()
