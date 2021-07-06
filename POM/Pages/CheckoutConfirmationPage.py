import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CheckoutConfirmationLocators():
    btn_confirm_order = (By.ID, "checkout_btn")




class CheckoutConfirmationPage():

    def __init__(self, driver):
        self.driver = driver


    def do_Checkout_Confirmation(self):
        return self.driver.find_element(*CheckoutConfirmationLocators.btn_confirm_order).click()

