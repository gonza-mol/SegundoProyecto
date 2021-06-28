from selenium.webdriver.common.by import By


class MyAccountPageLocators():
    text_my_account1 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.subtext")
    text_my_account2 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.maintext")
    btn_continue_register3 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>div>section>a")


class MyAccountPage():

    def __init__(self, driver):
        self.driver = driver

    def verificar_Ingreso_Correcto1(self):
        return self.driver.find_element(*MyAccountPageLocators.text_my_account1).text

    def verificar_Ingreso_Correcto2(self):
        return self.driver.find_element(*MyAccountPageLocators.text_my_account2).text

    def continue_Account3(self):
        self.driver.find_element(*MyAccountPageLocators.btn_continue_register3).click()
