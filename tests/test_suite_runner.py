from tests.home.login_tests import LoginTest
from tests.courses.enroll_course_tests_csv_data import EnrollCourseTest
import unittest

# Get all tests from the test class
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(EnrollCourseTest)

# create test suite
functional_tests = unittest.TestSuite([tc1, tc2])

# run the tes suite
unittest.TextTestRunner(verbosity=4).run(functional_tests)
