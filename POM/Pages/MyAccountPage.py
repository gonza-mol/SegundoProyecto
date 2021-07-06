import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MyAccountPageLocators():
      text_my_account1 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.subtext")
      text_my_account2 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.maintext")
      btn_continue_register3 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>div>section>a")
      text_account_created = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.maintext>i")
      makeup_btn = (By.CSS_SELECTOR, "#categorymenu>nav>ul>li:nth-child(3)>a")
      lips_option = (By.CSS_SELECTOR, "#categorymenu>nav>ul>li:nth-child(3)>div>ul:nth-child(1)>li:nth-child(4)>a")
      cart_option = (By.CSS_SELECTOR, "#main_menu_top>li:nth-child(3)>a>span")



class MyAccountPage():

    def __init__(self, driver):
        self.driver = driver

    def verificar_Ingreso_Correcto1(self):
        return self.driver.find_element(*MyAccountPageLocators.text_my_account1).text

    def verificar_Ingreso_Correcto2(self):
        return self.driver.find_element(*MyAccountPageLocators.text_my_account2).text

    def continue_Account3(self):
        self.driver.find_element(*MyAccountPageLocators.btn_continue_register3).click()

    def verificar_Created_Account_Success(self):
        return self.driver.find_element(*MyAccountPageLocators.text_account_created).text

    def seleccionar_Producto_Makeup(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*MyAccountPageLocators.makeup_btn))
        hover.perform()
        self.driver.find_element(*MyAccountPageLocators.lips_option).click()


    def seleccionar_Cart_Option(self):
        self.driver.find_element(*MyAccountPageLocators.cart_option).click()


