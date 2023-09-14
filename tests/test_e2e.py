import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import HomePage
from PageObjects.ShopPage import ShopPage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_One(self):

        self.driver.implicitly_wait(5)

        homePageObj = HomePage(self.driver)
        shopPageObj = homePageObj.click_shop()
        products = shopPageObj.cartItemSelect()

        for product in products:
            productNames = product.find_elements(By.XPATH, 'div/h4/a')
            for productName in productNames:
                if productName.text == 'Nokia Edge':
                    product.find_element(By.XPATH, "div/button").click()

        CheckOutPageObj = shopPageObj.clickOnCheckOutBtn()
        CheckOutPageObj.CheckOutBtn().click()
        CheckOutPageObj.EnterLocation().send_keys('ind')

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//a[text()="India"]')))
        self.driver.find_element(By.XPATH, '//a[text()="India"]').click()

        CheckOutPageObj.CheckBox().click()

        CheckOutPageObj.PurchaseBtnClick()

        msg = CheckOutPageObj.msgValidation()
        print(msg.text)