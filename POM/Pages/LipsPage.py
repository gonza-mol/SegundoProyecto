import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LipsPageLocators():
    btn_AddCart1 = (By.CSS_SELECTOR, "div:nth-child(3)>div.thumbnail>div.pricetag.jumbotron>a>i")


class LipsPage():

    def __init__(self, driver):
        self.driver = driver


    def add_Cart1(self):
        self.driver.find_element(*LipsPageLocators.btn_AddCart1).click()

    
