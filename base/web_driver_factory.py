from selenium import webdriver
import os


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = str(browser).lower()

    def getWebDriverInstance(self):
        baseUrl = "https://letskodeit.teachable.com/"
        if self.browser == "chrome":
            driverLocation = r"C:\pythonAutomation\chromedriver.exe"
            os.environ["webdriver.driver.chrome"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.implicitly_wait(3)
            driver.get(baseUrl)
        elif self.browser == "ie":
            driverLocation = r"C:\pythonAutomation\ie.exe"
            os.environ["webdriver.driver.ie"] = driverLocation
            driver = webdriver.Ie(driverLocation)
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(7)
        driver.get(baseUrl)
        return driver
