import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ShoppingCartLocators():
    btn_checkout = (By.CSS_SELECTOR, "#cart_checkout1")
    label_color = (By.CSS_SELECTOR, "tr:nth-child(2)>td:nth-child(2)>div>small")
    label_unit_price = (By.CSS_SELECTOR, "tr:nth-child(2)>td:nth-child(4)")
    label_qty = (By.ID, "cart_quantity59620a58973de6c7c5954c4ed2d88a0228")
    label_total = (By.CSS_SELECTOR, "tr:nth-child(2)>td:nth-child(6)")
    label_without_product = (By.XPATH, '//*[@class="contentpanel"]')
    label_with_product = (By.CSS_SELECTOR, "div.pull-left.coupon>table>tbody>tr:nth-child(1)>th")
    clean_shopping_cart = (By.CSS_SELECTOR, "table>tbody>tr:nth-child(2)>td:nth-child(7)>a")




class ShoppingCartPage():

    def __init__(self, driver):
        self.driver = driver


    def show_Color(self):
        return self.driver.find_element(*ShoppingCartLocators.label_color).text

    def show_Unit_Price(self):
        return self.driver.find_element(*ShoppingCartLocators.label_unit_price).text

    def show_Quantity(self):
        return self.driver.find_element(*ShoppingCartLocators.label_qty).get_attribute("value")

    def show_Total_Amount(self):
        return self.driver.find_element(*ShoppingCartLocators.label_total).text

    def do_Checkout(self):
        return self.driver.find_element(*ShoppingCartLocators.btn_checkout).click()

    def check_Label_Without_Element(self):
        return self.driver.find_element(*ShoppingCartLocators.label_without_product).text

    def check_Label_With_Element(self):
        return self.driver.find_element(*ShoppingCartLocators.label_with_product).text

    def clean_Shopping_Cart(self):
        self.driver.find_element(*ShoppingCartLocators.clean_shopping_cart).click()
