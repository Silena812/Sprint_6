import allure

from conftest import driver
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from curl import *


class MainPage(BasePage):

    def click_question(self, index):
        self.click_on_element(MainPageLocators.FAQ_QUESTIONS)[index].click()

    def get_answer_text(self, index):
        return self.get_text_on_element(MainPageLocators.FAQ_ANSWERS)[index].text

    def click_top_order_button(self):
        self.click_on_element(MainPageLocators.TOP_ORDER_BUTTON)

    def click_low_order_button(self):
        self.click_on_element(MainPageLocators.LOW_ORDER_BUTTON)

    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    def logo_yandex_goto_dzen(self):
        self.click_logo_yandex()
        self.switch_window()
        self.wait_for_url_contains("dzen.ru")
        return self.get_current_url()

    def click_logo_samokat(self):
        self.click_on_element(MainPageLocators.LOGO_SAMOKAT)

    def logo_samokat_goto_mainpage(self):
        self.click_logo_samokat()
        return self.get_current_url()