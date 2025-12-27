import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import Credentials
from curl import *

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()

    elif request.param == "firefox":
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture
def login_and_create_order(driver):
    login_page = LoginPage(driver)
    login_page.open_page(login_site)
    login_page.login(Credentials.email, Credentials.password)

    main_page = MainPage(driver)
    main_page.make_order()

    order_number = main_page.get_order_number()
    main_page.close_confirm_window()

    return driver, order_number
