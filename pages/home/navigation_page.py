from base.base_page import BasePage


class NavigatePage(BasePage):

    def __init__(self, driver):
        super(NavigatePage, self).__init__(driver)
        self.driver = driver

    # Define Locators
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings = "//div[@id='navbar']//li[@class='dropdown']"
    _home_image = "//a[@class='navbar-brand header-logo']//img"

    def navigateToAllCourses(self):
        return self.elementClick(locator=self._all_courses, locator_type="partiallink")

    def navigateToMyCourses(self):
        return self.elementClick(locator=self._my_courses, locator_type="partiallink")

    def navigateToPracticePage(self):
        return self.elementClick(locator=self._practice, locator_type="partiallink")

    def navigateToUserSettings(self):
        return self.elementClick(locator=self._user_settings, locator_type="xpath")

    def navigateToHomeImg(self):
        return self.elementClick(locator=self._home_image, locator_type="xpath")
