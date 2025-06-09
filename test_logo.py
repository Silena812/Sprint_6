import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *


def test_logo_samokat_goto_mainpage(driver):
    orderpage = OrderPage(driver)


    orderpage.click_logo_samokat()
    assert driver.current_url == main_site

def test_logo_yandex_goto_dzen(driver):
    mainpage = MainPage(driver)

    mainpage.click_logo_yandex()

    driver.switch_to.window(driver.window_handles[1])

    WebDriverWait(driver, 5).until(EC.url_contains("dzen.ru"))

    assert "dzen.ru" in driver.current_url