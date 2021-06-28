from _ast import Assert

from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
import time

from POM.Pages.CreateUserPage import CreateUserPage
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()




    def test_Login_success(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        time.sleep(2)
        lp = LandingPage(driver)
        lp.click_Go_Login()
        time.sleep(2)
        logpa = LoginPage(driver)
        time.sleep(2)
        logpa.submit_Username("gonza_mol")
        time.sleep(2)
        logpa.submit_Password("Chicharito10")
        time.sleep(2)
        logpa.click_Submit_Sign_In()
        time.sleep(2)
        account = MyAccountPage(driver)
        x = account.verificar_Ingreso_Correcto1()
        print(x)
        assert x == 'Gonzalo'
        print("Estoy dentro de la página de My account")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)
