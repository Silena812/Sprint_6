import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from pages.main_page import MainPage

from curl import *


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.headless = False
    service = Service()
    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1200, 900)
    driver.get(main_site)
    main_page = MainPage(driver)
    main_page.close_cookie_banner()

    yield driver
    driver.quit()