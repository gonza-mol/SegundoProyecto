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
import HtmlTestRunner


class CreateUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_create_New_Account(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        time.sleep(2)
        #Objeto creado de landingPage
        lp = LandingPage(driver)
        lp.click_Go_Login()
        time.sleep(2)

        #Objeto creado de LoginPage
        lop = LoginPage(driver)
        check = lop.verify_IsChecked()
        self.assertTrue(check, "Está la opción Create Account tildada")
        time.sleep(2)
        lop.submit_Continue()
        time.sleep(2)

        #Objeto creado de CreateUserPage
        account = CreateUserPage(driver)
        time.sleep(2)
        account.create_First_Name("Marcos")
        time.sleep(2)
        account.create_Last_Name("Zamora")
        time.sleep(2)
        account.create_Email("Marcos.Zamora@darwoft.com")
        time.sleep(2)
        account.create_Address1("Sol de Mayo 550")
        time.sleep(2)
        account.create_City("Cordoba")
        time.sleep(2)
        account.create_Zip_Code("5000")
        time.sleep(2)
        account.create_Country("Argentina")
        time.sleep(2)
        account.create_Region("Cordoba")
        time.sleep(2)
        account.create_Login_Name("Marcos_Zamora")
        time.sleep(2)
        account.create_Create_Password("River10")
        time.sleep(2)
        account.create_Confirm_Password("River10")
        time.sleep(2)
        account.create_Suscribe()
        time.sleep(2)
        account.create_Policy()
        time.sleep(2)
       # account.continue_Account2()
       # time.sleep(2)

       #Objeto Creado de MyAccountPage
       # myaccount = MyAccountPage(driver)
       # time.sleep(2)
       # myaccount.continue_Account3()
       # x = MyAccountPage.verificar_Ingreso_Correcto()
       # print(x)
       # assert x == 'MY ACCOUNT'
       # print("Estoy en la página de My account")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

