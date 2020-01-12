from pages.courses.resgister_course_page import RegisterCoursePage
from pages.home.navigation_page import NavigatePage
import unittest
import pytest
from utilities.test_status import TestStatus
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("set_up_one_time", "set_up")
@ddt
class EnrollCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, set_up_one_time):
        self.cp = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.np = NavigatePage(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for", "5565 4636 3463 4888", "0419", "128", "Canada", "201001"), ("Selenium WebDriver",
          "5565 4636 3463 4888", "0819", "234", "Canada", "206601"), ("Mac Linux", "5565 4636 3463 4888", "0919",
                                                                      "435", "Canada", "209901"))
    @unpack
    def test_invalidCardDetails(self, search_course, card_number, expiration_date, cvc_code, country, postal_code):
        self.cp.enrollCourse(search_course, card_number, expiration_date, cvc_code, country, postal_code)
        result = not (self.cp.verifyInvalidPaymentDetails())
        print("Result is : "+str(result))
        self.ts.mark_final_status("test_invalidCardDetails", result, "Invalid card details")
        self.cp.clickEnrollInCourse()
        self.np.navigateToHomeImg()



