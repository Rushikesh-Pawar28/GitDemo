import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


driver = None


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument('--start-maximized')
        option.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=option)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.get('https://rahulshettyacademy.com/angularpractice/')
    request.cls.driver = driver
    yield
    driver.close()
