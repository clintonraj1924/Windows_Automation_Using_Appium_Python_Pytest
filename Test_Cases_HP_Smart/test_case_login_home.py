from Page_Object.test_login_page import Login_Test


class Test_Login_Home:

    def test_login_page(self, setup):
        self.driver = setup

        # calling page object/test login page.py
        self.ls = Login_Test(self.driver)
        self.ls.test_hp_smart_signin()
