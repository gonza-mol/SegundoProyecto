import time
import pytest
import driver as driver
from pytest_bdd.parsers import string
from selenium import webdriver
import unittest
from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style

from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.ContactUsPage import ContactUsPage
import conftest
import HtmlTestRunner
import logging


AUTOMATION_PAGE = 'https://automationteststore.com/'
scenarios('../features/Verify_ContactUsForm.feature')

@given("I am on the Automation test logged in")
def step_Login(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    # ir a login page
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)
    # Esto permite el logueo
    logpa.do_Login("gonza_mol", "Chicharito10")



@when("I select the Contact Us option in the footer of the page,")
def step_SendRequest(browser):
    account = MyAccountPage(browser)
    account.seleccionar_ContactUs_Option()
    time.sleep(4)
    cu = ContactUsPage(browser)
    print(cu.verificar_ContactUs_Form())
    time.sleep(4)
    assert cu.verificar_ContactUs_Form() == "Contact Us Form"
    print(Fore.GREEN + "Estoy en la página de Contact Us")


@when(parsers.parse('Fill form name "{name}", email "{email}", Enquiry "{message}"'))
def step_FillForm(browser, name, email, message):
    cu = ContactUsPage(browser)
    time.sleep(4)
    cu.fill_FirstName(name)
    time.sleep(4)
    cu.fill_Email(email)
    time.sleep(4)
    cu.fill_Enquiry(message)
    time.sleep(4)
    cu.sendForm()



@then("I want to verify that my question has been sent successfully")
def step_Verify_successful_Sending_Request(browser):
    cu = ContactUsPage(browser)
    message = cu.Verify_Enquiry_Success()
    assert message == "Your enquiry has been successfully sent to the store owner!"



    if __name__ == '__main__':
        unittest.main()
