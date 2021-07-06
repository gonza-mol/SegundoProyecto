import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductPageLocators():
    list_color = (By.CSS_SELECTOR, "#option305")
    qty = (By.CSS_SELECTOR, "#product_quantity")
    btn_AddCart2 = (By.CSS_SELECTOR, "#product>fieldset>div:nth-child(5)>ul>li>a")



class ProductPage():

    def __init__(self, driver):
        self.driver = driver


    def select_Product_Lips_Color_And_Qty(self, color, qty):
        sel = Select(self.driver.find_element(*ProductPageLocators.list_color))
        sel.select_by_visible_text(color)
        self.driver.find_element(*ProductPageLocators.qty).clear()
        self.driver.find_element(*ProductPageLocators.qty).send_keys(qty)
        self.driver.find_element(*ProductPageLocators.btn_AddCart2).click()



