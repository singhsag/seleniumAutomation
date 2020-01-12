import pytest
from base.web_driver_factory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.yield_fixture()
def set_up():
    print("Running conftest before every test")
    yield
    print("Running conftest after every test")


# to run once at module or class level

@pytest.yield_fixture(scope="class")
def set_up_one_time(request, browser):
    print("One time before module")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("One time after module")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
