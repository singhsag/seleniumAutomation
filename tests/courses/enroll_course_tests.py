from pages.courses.resgister_course_page import RegisterCoursePage
import unittest
import pytest
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("set_up_one_time", "set_up")
class EnrollCourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, set_up_one_time):
        self.cp = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidCardDetails(self):
        self.cp.enrollCourse("JavaScript for", "5565 4636 3463 4888", "0419", "128", "Canada", "201001")
        result = not (self.cp.verifyInvalidPaymentDetails())
        print("Result is : "+str(result))
        self.ts.mark_final_status("test_invalidCardDetails", result, "Invalid card details")
        self.cp.clickEnrollInCourse()
