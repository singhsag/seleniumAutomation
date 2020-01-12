from pages.courses.resgister_course_page import RegisterCoursePage
from pages.home.navigation_page import NavigatePage
import unittest
import pytest
from utilities.test_status import TestStatus
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from utilities.get_csv_data import getCsvData


@pytest.mark.usefixtures("set_up_one_time", "set_up")
@ddt
class EnrollCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, set_up_one_time):
        self.cp = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.np = NavigatePage(self.driver)

    def setUp(self):
        self.np.navigateToHomeImg()

    @pytest.mark.run(order=1)
    @data(*getCsvData("C:\\Users\\sagar\\PycharmProjects\\LetsKodeIt\\test_data.csv"))
    @unpack
    def test_invalidCardDetails(self, search_course, card_number, expiration_date, cvc_code, country, postal_code):
        self.cp.enrollCourse(search_course, card_number, expiration_date, cvc_code, country, postal_code)
        result = not (self.cp.verifyInvalidPaymentDetails())
        print("Result is : "+str(result))
        self.ts.mark_final_status("test_invalidCardDetails", result, "Invalid card details")
        self.cp.clickEnrollInCourse()
        self.np.navigateToHomeImg()



