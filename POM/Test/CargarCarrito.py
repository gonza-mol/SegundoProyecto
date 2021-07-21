from _ast import Assert

from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import time
from selenium.webdriver.support.select import Select

from POM.Pages.CreateUserPage import CreateUserPage
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.SkinCarePage import SkinCarePage
import HtmlTestRunner


class CargarCarrito(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_CargarCarrito(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        lp = LandingPage(driver)
        skp = SkinCarePage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        logpa.do_Login("gonza_mol", "Chicharito10")
        my = MyAccountPage(driver)
        time.sleep(2)
        my.seleccionar_Producto_SkinCare()
        time.sleep(4)
        driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(4)
        skp.add_Product_Antiage()
        time.sleep(2)
        skp.add_Product_Cremenuit()
        time.sleep(2)
        skp.add_Product_Facialcream()
        time.sleep(2)
        skp.add_Product_Absolueyes()
        time.sleep(2)
        my.seleccionar_Logoff()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

