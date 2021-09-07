import time

import json
import pytest
from pytest_bdd import given
from selenium import webdriver
import selenium.webdriver

#constants
#AUTOMATION_PAGE = 'https://automationteststore.com/'


@pytest.fixture()
def browser():
    b = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.quit()


'''
@pytest.fixture()
def config(scope='session'):
    with open('config.json') as config_file:
      config = json.load(config_file)
    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return config


@pytest.fixture(config)
def browser():
    if config['browser'] == 'Chrome':
        b = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
        #b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    b.implicitly_wait(config['implicit_wait'])
    b.maximize_window()
    yield b
    b.quit()
'''