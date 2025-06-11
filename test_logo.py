import pytest
import allure
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *

class TestLogo:

    @allure.title("Проверяем переход с лого Самокат на главную страницу")
    def test_logo_samokat_goto_mainpage(self,driver):
        mainpage = MainPage(driver)
        url = mainpage.logo_samokat_goto_mainpage()
        assert url == main_site

    @allure.title("Проверяем переход с лого Самокат на главную страницу")
    def test_logo_yandex_goto_dzen(self,driver):
        mainpage = MainPage(driver)
        url = mainpage.logo_yandex_goto_dzen()

        assert "dzen.ru" in url