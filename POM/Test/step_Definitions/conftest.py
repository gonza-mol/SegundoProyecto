import time

import pytest
from pytest_bdd import given
from selenium import webdriver

#constants
#AUTOMATION_PAGE = 'https://automationteststore.com/'


@pytest.fixture()
def browser():
    b = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.quit()