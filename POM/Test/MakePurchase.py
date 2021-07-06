from _ast import Assert

from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import colorama
from colorama import Fore, Back, Style
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

import time

from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.LipsPage import LipsPage
from POM.Pages.ProductPage import ProductPage
from POM.Pages.ShoppingCartPage import ShoppingCartPage
from POM.Pages.CheckoutConfirmationPage import CheckoutConfirmationPage
from POM.Pages.CheckoutStatus import CheckoutStatus
import HtmlTestRunner


class MakePurchase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Purchase_success(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        time.sleep(2)
        #ir a login page
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)

        #Esto permite el logueo
        logpa.do_Login("gonza_mol", "Chicharito10")
        time.sleep(2)

        #Verifico que no tenga nada en el carrito de Compras
        scp = ShoppingCartPage(driver)
        my = MyAccountPage(driver)

        my.seleccionar_Cart_Option()

        try:
            assert scp.check_Label_Without_Element() == 'Your shopping cart is empty!\nContinue'
            my.seleccionar_Producto_Makeup()
        except:
            scp.clean_Shopping_Cart()
            print("Había un producto seleccionado con anterioridad, se va eliminar el mismo")
            my.seleccionar_Producto_Makeup()

        time.sleep(2)
        lip = LipsPage(driver)
        lip.add_Cart1()
        time.sleep(2)

        #Acá del tipo de producto elegido, selecciono el color, y la cantidad y verifico que coincido lo que pido
        print("Datos del nuevo producto seleccionado:")
        pp = ProductPage(driver)
        pp.select_Product_Lips_Color_And_Qty("Viva Glam II", "3")
        time.sleep(2)
        #scp = ShoppingCartPage(driver)
        assert scp.show_Color() == 'Color Viva Glam II'
        print(Fore.GREEN + "El color elegido es: "+scp.show_Color())
        time.sleep(2)
        assert scp.show_Unit_Price() == '$5.00'
        print(Fore.GREEN + "El precio unitario del producto es: "+scp.show_Unit_Price())
        time.sleep(2)
        assert scp.show_Quantity() == '3'
        print(Fore.GREEN + "La cantidad del producto elegido es: " + scp.show_Quantity())
        time.sleep(2)
        assert scp.show_Total_Amount() == '$15.00'
        print(Fore.GREEN + "El precio total de los productos elegidos es: " + scp.show_Total_Amount())
        time.sleep(2)
        scp.do_Checkout()
        time.sleep(2)

        #Acá ya confirmo el pedido
        ccp = CheckoutConfirmationPage(driver)
        ccp.do_Checkout_Confirmation()
        time.sleep(2)

        #Acá ya obtengo la confirmación exitosa del pedido
        cs = CheckoutStatus(driver)
        time.sleep(2)
        assert cs.get_Message_Alternative() == 'You can view your order details by going to the invoice page.'
        time.sleep(2)
        print(Fore.GREEN + "La orden ha sido procesada exitosamente")
        time.sleep(2)
        cs.select_Button_Continue()
        time.sleep(2)

        #Acá verifico que una vez comprado el producto, vuelva a la Landing Page (homepage)
        assert lp.verificar_Nombre_Landing_Page() == 'Welcome back Gonzalo'
        print(Fore.BLUE + "Estas en la página Home")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

