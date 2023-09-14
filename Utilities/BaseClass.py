import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def ExplicitWait(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[text()="India"]')))
        self.driver.find_element(By.XPATH, '//a[text()="India"]')