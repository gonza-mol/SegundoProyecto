import re
import time
import pytest
import driver as driver
from pytest_bdd.parsers import string
from selenium import webdriver
import unittest
from functools import partial
from pytest_bdd import scenarios, given, when, then
from colorama import Fore, Back, Style
from selenium.common.exceptions import NoSuchElementException
from POM.Pages.LandingPage import LandingPage
from POM.Pages.LoginPage import LoginPage
from POM.Pages.MyAccountPage import MyAccountPage
from POM.Pages.LipsPage import LipsPage
from POM.Pages import ProductPage
from POM.Pages.ShoppingCartPage import ShoppingCartPage
from POM.Pages.CheckoutConfirmationPage import CheckoutConfirmationPage
from POM.Pages.My_Order_History import My_Order_History
import HtmlTestRunner
import logging



AUTOMATION_PAGE = 'https://automationteststore.com/'


scenarios('../features/Verify_ElementsOfMenu.feature')

@given("I am on the Automation test store page login")
def step_login(browser):
    browser.get(AUTOMATION_PAGE)
    time.sleep(2)
    # ir a login page
    lp = LandingPage(browser)
    lp.click_Go_Login()
    logpa = LoginPage(browser)
    time.sleep(2)


@when("I am on the My Account page, i verify the number of Items that exist in the menu")
def step_VerifyNumberOfElements(browser):
    account = MyAccountPage(browser)


@then("I return the number of items/columns, and each of the menu items.")
def step_ShowElementsMenu(browser):
    account = MyAccountPage(browser)
    n = account.getNumberMenuItems()
    print(Fore.RED + Style.BRIGHT + "La cantidad de elementos en el menú es: " + str(n) + Style.RESET_ALL)
    time.sleep(2)
    m = account.getMenuItems()
    print(Fore.MAGENTA + "Los elementos del menú son: \n")
    time.sleep(2)
    aux = 0
    items = ['HOME', '  APPAREL & ACCESSORIES', '  MAKEUP', '  SKINCARE', '  FRAGRANCE', '  MEN', '  HAIR CARE',
             '  BOOKS']
    for idx, menu in enumerate(m, start=1):
        assert menu.text == items[aux]
        aux = aux + 1
        print(Style.BRIGHT + Fore.MAGENTA + str(idx), menu.text)

    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)

