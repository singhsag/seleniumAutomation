from base.selenium_driver import SeleniumDriver
from utilities.util import Util
import utilities.custom_logger as cl
import logging


class BasePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.ut = Util()

    def verifyPageTitle(self, expected_title):

        actual_title = self.getTitle()
        try:
            return self.ut.verifyTextContains(actual_title, expected_title)
        except:
            self.log.error("Exception Occurred")
            return False
