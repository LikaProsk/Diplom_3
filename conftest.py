import json
import random
import string

import pytest
import requests
from selenium import webdriver

from urls.site_urls import URL_REG_USER, URL_DEL_USER


def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome", help="Укажите имя браузера для запуска тестов")


@pytest.fixture()
def driver(get_browser_name):
    if get_browser_name == "firefox":
        driver = webdriver.Firefox()
    elif get_browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture()
def get_browser_name(request):
    return request.config.getoption("--browserName")


@pytest.fixture()
def reg_name():
    names = ['Lika', 'Ivan', 'Petr', 'Roman']
    return names[random.randint(0, len(names) - 1)]


@pytest.fixture()
def reg_email():
    return f"user{random.randint(0, 10000)}@mail.ru"


@pytest.fixture()
def reg_password(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@pytest.fixture()
def create_user(reg_email, reg_password, reg_name):
    payload = {
        "email": reg_email,
        "password": reg_password,
        "name": reg_name
    }

    response = requests.post(URL_REG_USER, data=payload)

    assert response.status_code == 200

    yield payload

    access_token = json.loads(response.text).get("accessToken")
    requests.delete(URL_DEL_USER, headers={"Authorization": access_token})
