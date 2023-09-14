from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    finalCheckOutBtn = (By.XPATH, "//button[@class='btn btn-success']")
    location = (By.ID, 'country')
    checkBox = (By.XPATH, '//label[@for="checkbox2"]')
    purchaseBtn = (By.XPATH, "//input[contains(@class,'success')]")
    msg = (By.XPATH, '//div[contains(@class,"success")]')


    def CheckOutBtn(self):
        return self.driver.find_element(*CheckOutPage.finalCheckOutBtn)

    def EnterLocation(self):
        return self.driver.find_element(*CheckOutPage.location)

    def CheckBox(self):
        return self.driver.find_element(*CheckOutPage.checkBox)

    def PurchaseBtnClick(self):
        return self.driver.find_element(*CheckOutPage.purchaseBtn).click()

    def msgValidation(self):
        return self.driver.find_element(*CheckOutPage.msg)