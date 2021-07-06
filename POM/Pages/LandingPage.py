from selenium.webdriver.common.by import By

class LandingPageLocators():
    go_Login = (By.CSS_SELECTOR, "#customer_menu_top>li>a")
    label_name = (By.CSS_SELECTOR, "#customer_menu_top>li>a>div")

class LandingPage():

    def __init__(self, driver):
        self.driver = driver

    def click_Go_Login(self):
        self.driver.find_element(*LandingPageLocators.go_Login).click()

    def verificar_Nombre_Landing_Page(self):
        return self.driver.find_element(*LandingPageLocators.label_name).text


