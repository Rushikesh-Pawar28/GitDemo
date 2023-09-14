from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage


class ShopPage:
    def __init__(self,driver):
        self.driver = driver

    cartItems = (By.XPATH, "//div[contains(@class,'card h-100')]")
    productNames = (By.XPATH, 'div/h4/a')
    checkOutBtn = (By.XPATH, "//a[contains(@class,'nav-link btn btn-primary')]")

    def cartItemSelect(self):
        return self.driver.find_elements(*ShopPage.cartItems)

    def selectProduct(self):
        return self.cartItemSelect().find_elements(*ShopPage.productNames)

    def clickOnCheckOutBtn(self):
        self.driver.find_element(*ShopPage.checkOutBtn).click()
        CheckOutPageObj = CheckOutPage(self.driver)
        return CheckOutPageObj