# from base.selenium_driver import SeleniumDriver
from base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver

    # Define Locators
    _login_link = "//a[@href='/sign_in']"
    _user_field = "user_email"
    _pass_field = "user_password"
    _login_btn = "commit"
    _verify_login_user = "//img[@class='gravatar']"  # user image setting icon
    _verify_login_failed = "//div[contains(text(),'Invalid email or password')]"
    _logout_user = "//a[contains(text(),'Log Out')]"

    def clickLoginLink(self):
        self.elementClick(self._login_link, "xpath")

    def enterEmail(self, username):
        self.sendKeys(username, self._user_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._pass_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn, "name")

    def clearEmail(self):
        self.clearKeys(self._user_field)

    def clearPassword(self):
        self.clearKeys(self._pass_field)

    # Call actual login method, This is Functionality
    def login(self, username="", password=""):
        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginBtn()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._verify_login_user, locator_type="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._verify_login_failed, locator_type="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        # user_settings = self.waitForElement(self._verify_login_user, "xpath")
        self.elementClick(self._verify_login_user, "xpath")
        self.elementClick(self._logout_user, "xpath")
