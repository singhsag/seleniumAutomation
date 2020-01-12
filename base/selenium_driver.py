from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from traceback import print_stack
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshots(self, request_message):
        file_name = request_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshots_dir = "..\\screenshots\\"
        relative_file_name = screenshots_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_file_name)
        self.log.info("Destination File Name" + destination_file)
        destination_dir = os.path.join(current_dir, screenshots_dir)
        self.log.info("Destination Director" + destination_dir)

        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to " + destination_file)
        except:
            self.log.error("Exception Occurred")
            print_stack()

    def refreshCurrentPage(self):
        return self.driver.refresh()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locator_type="id"):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partiallink":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        else:
            print("Not a valid Locator Type")

    def getElement(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f'Found Element with locator: {locator} and locator_type: {locator_type}')
        except:
            self.log.error(f'Element Not Found with locator: {locator} and locator_type: {locator_type}')
            print_stack()
        return element

    def getElements(self, locator, locator_type="id"):
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info(f'Found Element with locator: {locator} and locator_type: {locator_type}')
        except:
            self.log.error(f'Element Not Found with locator: {locator} and locator_type: {locator_type}')
            print_stack()
        return elements

    def elementClick(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        try:
            if locator:  # This means if locator is not empty
                locator_type = locator_type.lower()
                element = self.getElement(locator, locator_type)
            element.click()
            self.log.info(f'Clicked Element with locator: {locator} and locator_type: {locator_type}')
        except:
            self.log.error(f'Not able to click element with locator: {locator} and locator_type: {locator_type}')
            print_stack()

    def sendKeys(self, data, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        try:
            if locator:
                locator_type = locator_type.lower()
                element = self.getElement(locator, locator_type)
            element.send_keys(data)
            self.log.info(f'Sent data to Element with locator: {locator} and locator_type: {locator_type}')
        except:
            self.log.error(f'Not able to send data to element with locator: {locator} and locator_type: {locator_type}')
            print_stack()

    def getText(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        try:
            if locator:
                locator_type = locator_type.lower()
                element = self.getElement(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            self.log.info(f'Text found on element {element} is {text}')
        except:
            self.log.error(f'Not able to found text on element {element} : {text}')
            print_stack()
        return text

    def getElementAttributeValue(self,element=None, attribute="", locator="", locator_type="id", ):
        """
        Either provide Element or a combination of both locator and locator type
        """
        try:
            if locator:
                locator_type = locator_type.lower()
                element = self.getElement(locator, locator_type)
            value = element.get_attribute(attribute)
            self.log.info(f'Text found on element {element} is {value}')
        except:
            self.log.error(f'Not able to found text on element {element} : {value}')
        return value

    def clearKeys(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        try:
            if locator:
                locator_type = locator_type.lower()
                element = self.getElement(locator, locator_type)
            element.clear()
            self.log.info(f'Clear data to Element with locator: {locator} and locator_type: {locator_type}')
        except:
            self.log.info(f'Not able to clear data to element with locator: {locator} and locator_type: {locator_type}')
            print_stack()

    def selectDropdownByText(self, visible_text, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        try:
            if locator:
                locator_type = locator_type.lower()
                element = self.getElement(locator, locator_type)
            sel = Select(element)
            sel.select_by_visible_text(visible_text)
            self.log.info(f'Element {element} selected by text {visible_text}')
        except:
            self.log.error(f'Could not select Element {element} by text {visible_text}')

    def switchToIframe(self, reference):
        """
        Reference can be iFrame Id, Name or Number
        """
        try:
            self.driver.switch_to.frame(reference)
            self.log.info(f'Switched to iFrame with reference {reference}')
        except:
            self.log.error(f'Could not Switched to iFrame with reference {reference}')

    def switchToParentframe(self):
        """
        Reference can be iFrame Id, Name or Number
        """
        try:
            self.driver.switch_to.default_content()
            self.log.info(f'Switched to parent iFrame')
        except:
            self.log.error(f'Could not able to Switched to parent iFrame')

    def isElementPresent(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        try:
            if locator:
                locator_type = locator_type.lower()
                by_type = self.getByType(locator_type)
                element = self.driver.find_element(by_type, locator)

            if element is not None:
                self.log.info(f'Element present with locator: {locator} and locator_type: {locator_type}')
                return True
            else:
                self.log.error(f"Element Not present with locator: {locator} and locator_type: {locator_type}")
                return False
        except:
            self.log.error("Element not present with locator: {locator} and locator_type: {locator_type}'")
            return False

    def isEnabled(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        Check for Element disable based on 'disabled' attribute or presence of disabled in any other attribute
        """
        try:
            if locator:
                locator_type = locator_type.lower()
                by_type = self.getByType(locator_type)
                element = self.driver.find_element(by_type, locator)

                attribute_value = self.getElementAttributeValue(element, attribute="disabled")
                if attribute_value is not None:
                    self.log.info(f'[isEnabled] Element present with locator: {locator} and locator_type: '
                                  f'{locator_type} value {attribute_value}')
                    return False
                else:
                    attribute_value = self.getElementAttributeValue(element, attribute="class")
                    self.log.error(f"[isEnabled] Element present with locator: {locator} and locator_type: "
                                   f"{locator_type} value {attribute_value}")
                    return not ("disabled" in attribute_value)
        except:
            self.log.error("[isEnabled] Element not present with locator: {locator} and locator_type: {locator_type}'")
            return False

    def isElementDisplayed(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        is_displayed = False
        try:
            if locator:
                locator_type = locator_type.lower()
                by_type = self.getByType(locator_type)
                element = self.driver.find_element(by_type, locator)

            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info(f'Element is displayed with locator: {locator} and locator_type: {locator_type}')
                return is_displayed
            else:
                self.log.error(f"Element not displayed with locator: {locator} and locator_type: {locator_type}")
                return is_displayed
        except:
            self.log.error(f"Element not displayed with locator: {locator} and locator_type: {locator_type}'")
            return False

    def isElementSelected(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        is_selected = False
        try:
            if locator:
                locator_type = locator_type.lower()
                by_type = self.getByType(locator_type)
                element = self.driver.find_element(by_type, locator)

            if element is not None:
                is_selected = element.is_selected()
                self.log.info(f'Element is selected with locator: {locator} and locator_type: {locator_type}')
                return is_selected
            else:
                self.log.error(f"Element not selected with locator: {locator} and locator_type: {locator_type}")
                return is_selected
        except:
            self.log.error(f"Element not selected with locator: {locator} and locator_type: {locator_type}'")
            return False

    def isElementEnabled(self, locator="", locator_type="id", element=None):
        """
        Either provide Element or a combination of both locator and locator type
        """
        is_enabled = False
        try:
            if locator:
                locator_type = locator_type.lower()
                by_type = self.getByType(locator_type)
                element = self.driver.find_element(by_type, locator)

            if element is not None:
                is_displayed = element.is_enabled()
                self.log.info(f'Element is enabled with locator: {locator} and locator_type: {locator_type}')
                return is_enabled
            else:
                self.log.error(f"Element not enabled with locator: {locator} and locator_type: {locator_type}")
                return is_enabled
        except:
            self.log.error(f"Element not enabled with locator: {locator} and locator_type: {locator_type}'")
            return False

    def waitForElement(self, locator, locator_type="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            wait = WebDriverWait(self.driver, timeout=timeout, pollFrequency=pollFrequency, ignored_exceptions=
            [ElementNotVisibleException,
             NoSuchElementException,
             ElementNotSelectableException])
            element = wait.until(EC.element_located_to_be_selected((by_type, locator)))
            self.log.info(f"Wait Element Found with locator: {locator} and locator_type: {locator_type}")
        except:
            self.log.error(f"Wait Element not found with locator: {locator} and locator_type: {locator_type}")
        return element

    def webScroll(self, direction="up"):
        if direction.lower() == "up":
            self.driver.execute_script("window.scrollBy(0,-500);")

        if direction.lower() == "down":
            self.driver.execute_script("window.scrollBy(0,500);")
