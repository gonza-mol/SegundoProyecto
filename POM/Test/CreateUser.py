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
        account.complete_All_Field_For_New_Account("Lukages", "Cornejoss", "Lukage.Cornejoss@darwoft.com", "Sol de Mayo 550", "Cordoba", "5000", "Lukages_Cornejoss", "River10", "River10")
        time.sleep(2)
        account.create_Country("Argentina")
        time.sleep(2)
        account.create_Region("Cordoba")
        time.sleep(2)
        account.submit_Button_Continue_whitout_Mandatory_field()

       #Objeto Creado de MyAccountPage
        myaccount = MyAccountPage(driver)
        time.sleep(2)
        myaccount.continue_Account3()
        time.sleep(2)
        x = myaccount.verificar_Ingreso_Correcto2()
        time.sleep(2)
        print(x)
        assert x == 'MY ACCOUNT'
        print("Estoy en la página de My account, se ha creado exitosamente la cuenta del nuevo usuario")



    def test_create_New_Account_Without_Mandatory_Fields(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        time.sleep(2)
        #Objeto creado de landingPage
        lp = LandingPage(driver)
        lp.click_Go_Login()
        time.sleep(2)

        #Objeto creado de LoginPage
        lop = LoginPage(driver)
        time.sleep(2)
        lop.submit_Continue()
        time.sleep(2)

        #Acá se dejan todos los campos mandatorios vacíos y se selecciona el botón continuar
        cup = CreateUserPage(driver)
        time.sleep(2)
        cup.submit_Button_Continue_whitout_Mandatory_field()
        time.sleep(2)
        x = cup.show_error_Mandatory_Field()
        assert x == '×\nError: You must agree to the Privacy Policy!'
        print("Error al no ingresar campos mandatorios")
        assert cup.show_Mandatory_Field_First_Name() == 'First Name must be between 1 and 32 characters!'
        assert cup.show_Mandatory_Field_Last_Name() == 'Last Name must be between 1 and 32 characters!'
        assert cup.show_Mandatory_Field_Email() == 'Email Address does not appear to be valid!'
        assert cup.show_Mandatory_Field_Address() == 'Address 1 must be between 3 and 128 characters!'
        assert cup.show_Mandatory_Field_City() == 'City must be between 3 and 128 characters!'
        assert cup.show_Mandatory_Field_Region() == 'Please select a region / state!'
        assert cup.show_Mandatory_Field_Zipcode() == 'Zip/postal code must be between 3 and 10 characters!'
        assert cup.show_Mandatory_Field_LoginName() == 'Login name must be alphanumeric only and between 5 and 64 characters!'
        assert cup.show_Mandatory_Field_Password() == 'Password must be between 4 and 20 characters!'


    def test_Verify_User_Has_Already_Been_Created(self):
        driver = self.driver
        driver.get("https://automationteststore.com/")
        time.sleep(2)
        # Objeto creado de landingPage
        lp = LandingPage(driver)
        lp.click_Go_Login()
        time.sleep(2)

        # Objeto creado de LoginPage
        lop = LoginPage(driver)
        time.sleep(2)
        lop.submit_Continue()
        time.sleep(2)

        # Objeto creado de CreateUserPage
        account = CreateUserPage(driver)
        time.sleep(2)
        account.complete_All_Field_For_New_Account("Gonzalo", "Molina", "gonzalo.molina@darwoft.com",
                                                   "Sol de Mayo 550", "Cordoba", "5000", "gonza_mol", "Chicharito10", "Chicharito10")

        time.sleep(2)
        account.create_Country("Argentina")
        time.sleep(2)
        account.create_Region("Cordoba")
        time.sleep(2)
        account.submit_Button_Continue_whitout_Mandatory_field()
        time.sleep(2)
        x = account.show_Existing_User_Message()
        print(x)
        assert x == '×\nError: E-Mail Address is already registered!'
        print("Error al querer crear una cuenta de un usuario ya existente")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

