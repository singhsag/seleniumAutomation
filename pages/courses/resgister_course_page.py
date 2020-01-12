from base.base_page import BasePage
from utilities.custom_logger import customLogger
import logging
import time


class RegisterCoursePage(BasePage):
    def __init__(self, driver):
        super(RegisterCoursePage, self).__init__(driver)
        self.driver = driver
        self.log = customLogger(logging.DEBUG)

    # Define locators
    _category_options = "//div[@class='filter-label'][contains(text(),'Category')]//following-sibling::div//button"
    _category_All = "//div[@class='btn-group open']//a[contains(text(),'All')]"
    _find_course = "search-courses"  # id
    # _javascript_course = "//div[@class='course-listing-title'][contains(text(),"+search_course")]"
    _dynamic_js_course = None
    _enroll_course = "enroll-button-top"  # id
    _card_number_iFrame = "__privateStripeFrame8"
    _card_number = "cardnumber"  # name
    _expiration_date_iFrame = "__privateStripeFrame9"
    _expiration_date = "exp-date"  # name
    _cvc_code_iFrame = "__privateStripeFrame10"
    _cvc_code = "cvc"  # name
    _country_dd = "country_code_credit_card-cc"  # id
    _postal_code_iFrame = "__privateStripeFrame11"
    _postal_code = "postal"  # name
    _save_payment_details = "save-payment-details"  # id
    _agree_terms = "agreed_to_terms_checkbox"  # id
    _enroll_in_course = "//button[@id='confirm-purchase']"

    def clickCategoryOption(self):
        return self.elementClick(self._category_options, "xpath")

    def clickAllCategory(self):
        return self.elementClick(self._category_All, "xpath")

    def searchCourse(self, search_course):
        return self.sendKeys(search_course, self._find_course)

    def selectSearchedCourse(self, search_course):
        _javascript_course = "//div[@class='course-listing-title'][contains(text(),'SELECT_COURSE')]"
        self._dynamic_js_course = _javascript_course.replace("SELECT_COURSE", search_course)
        # print("Dynamic xpath : "+self._dynamic_js_course)
        # self.waitForElement(self._dynamic_js_course, "xpath")
        return self.elementClick(self._dynamic_js_course, "xpath")

    def clickEnrollCourse(self):
        return self.elementClick(self._enroll_course)

    def scrollEnrollPage(self):
        return self.webScroll("down")

    def switchToParentIframe(self):
        self.switchToParentframe()

    def enterCardNumber(self, card_number):
        self.switchToIframe(self._card_number_iFrame)
        return self.sendKeys(card_number, self._card_number, "name")

    def enterExpirationDate(self, expiration_date):
        self.switchToIframe(self._expiration_date_iFrame)
        return self.sendKeys(expiration_date, self._expiration_date, "name")

    def enterCvcCode(self, cvc_code):
        self.switchToIframe(self._cvc_code_iFrame)
        return self.sendKeys(cvc_code, self._cvc_code, "name")

    def selectCountry(self, visible_text):
        return self.selectDropdownByText(visible_text, self._country_dd)

    def enterPostalCode(self, postal_code):
        self.switchToIframe(self._postal_code_iFrame)
        return self.sendKeys(postal_code, self._postal_code, "name")

    def checkSavePayment(self):
        if self.isElementSelected(self._save_payment_details):
            pass
        else:
            return self.elementClick(self._save_payment_details)

    def checkAgreeTerms(self):
        if self.isElementSelected(self._agree_terms):
            pass
        else:
            return self.elementClick(self._agree_terms)

    def checkEnrollInCourse(self):
        return self.isEnabled(self._enroll_in_course, "xpath")

    def clickEnrollInCourse(self):
        if self.checkEnrollInCourse():
            self.elementClick(self._enroll_in_course, "xpath")

    def enterPaymentDetails(self, card_number, expiration_date, cvc_code, country, postal_code):
        self.enterCardNumber(card_number)
        self.enterExpirationDate(expiration_date)
        self.enterCvcCode(cvc_code)
        self.selectCountry(country)
        self.enterPostalCode(postal_code)

    def enrollCourse(self, search_course, card_number, expiration_date, cvc_code, country, postal_code):
        self.clickCategoryOption()
        self.clickAllCategory()
        self.searchCourse(search_course)
        self.selectSearchedCourse(search_course)
        self.clickEnrollCourse()
        self.scrollEnrollPage()
        self.enterCardNumber(card_number)
        self.switchToParentIframe()
        self.enterExpirationDate(expiration_date)
        self.switchToParentIframe()
        self.enterCvcCode(cvc_code)
        self.switchToParentIframe()
        self.selectCountry(country)
        self.enterPostalCode(postal_code)
        self.switchToParentIframe()
        self.checkSavePayment()
        self.checkAgreeTerms()

    def verifyInvalidPaymentDetails(self):
        return self.checkEnrollInCourse()

    def FinalEnroll(self):
        if self.verifyPaymentDetails():
            self.clickEnrollInCourse()
        else:
            pass
