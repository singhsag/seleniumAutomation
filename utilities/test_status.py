from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def setResult(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### Verification Successful ### " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.info("### Verification Failed ### " + result_message)
                    self.screenshots(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.info("### Verification Failed ### " + result_message)
                self.screenshots(result_message)
        except:
            self.result_list.append("FAIL")
            self.log.error("### Exception occurred ### " + result_message)
            self.screenshots(result_message)

    def mark_status(self, result, result_message):
        self.setResult(result, result_message)

    def mark_final_status(self, test_name, result, result_message):
        self.setResult(result, result_message)
        if "FAIL" in self.result_list:
            self.log.error(test_name + " ### Test Failed")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### Test Passed")
            self.result_list.clear()
            assert True == True
