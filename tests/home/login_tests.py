from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("set_up_one_time", "set_up")
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetUp(self, set_up_one_time):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark_status(result1, "Title is Incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.mark_final_status("test_validLogin", result2, "Login not successful")

    # This is commented since we are logging by default in conftest.py , will handle this later
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
        self.lp.clearEmail()
        self.lp.clearPassword()
