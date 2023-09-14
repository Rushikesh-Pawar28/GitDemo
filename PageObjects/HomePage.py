from selenium.webdriver.common.by import By

from PageObjects.ShopPage import ShopPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shopBtn = (By.XPATH, "//a[text()='Shop']")

    def click_shop(self):
        self.driver.find_element(*HomePage.shopBtn).click()
        shopPageObj = ShopPage(self.driver)
        return shopPageObj

