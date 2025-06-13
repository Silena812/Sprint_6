import allure

from pages.base_page import BasePage
from locators.make_order_locators import MakeOrderLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step("Указать имя")
    def set_first_name(self, first_name):
        self.send_keys_to_input(MakeOrderLocators.FIRST_NAME, first_name)

    @allure.step("Указать фамилию")
    def set_last_name(self, last_name):
        self.send_keys_to_input(MakeOrderLocators.LAST_NAME, last_name)

    @allure.step("Указать адрес")
    def set_address(self, address):
        self.send_keys_to_input(MakeOrderLocators.ADDRESS, address)

    @allure.step("Выбрать станцию метро")
    def set_metro(self, metro_search, metro_partial):
        self.send_keys_to_input(MakeOrderLocators.METRO_INPUT, metro_search)
        options = self.find_elements(MakeOrderLocators.METRO_OPTIONS)

        for option in options:
            if metro_partial in option.text:
                option.click()
                break

    @allure.step("Указать телефон")
    def set_phone(self, phone):
        self.send_keys_to_input(MakeOrderLocators.PHONE, phone)

    @allure.step("Кликнуть на кнопку Далее")
    def click_next_button(self):
        self.click_on_element(MakeOrderLocators.NEXT_BUTTON)

    @allure.step("Указать дату доставки")
    def set_date(self, date):
        self.send_keys_to_input(MakeOrderLocators.DATE, date)
        self.send_keys_to_input(MakeOrderLocators.DATE, Keys.ENTER)

    @allure.step("Выбрать срок аренды")
    def set_period(self, period_text):
        self.click_on_element(MakeOrderLocators.PERIOD_DROPDOWN)  # открыть дропдаун

        period_options = self.find_elements(MakeOrderLocators.PERIOD_OPTIONS, timeout=5)

        for option in period_options:
            if option.text == period_text:
                option.click()
                break

    @allure.step("Выбрать цвет")
    def set_color(self, color):
        xpath = MakeOrderLocators.COLOR_CHECKBOX_TEMPLATE.format(color)
        self.click_on_element((By.XPATH, xpath))

    @allure.step("Добавить комментарий")
    def set_comment(self, comment):
        self.send_keys_to_input(MakeOrderLocators.COMMENT, comment)

    @allure.step("Кликнуть на кнопку Заказать")
    def click_order_button(self):
        self.click_on_element(MakeOrderLocators.ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку Да в окне подтверждения заказа")
    def click_confirmation_button(self):
        self.click_on_element(MakeOrderLocators.CONFIRMATION_BUTTON)

    @allure.step("Сделать заказ целиком")
    def make_order(self, first_name, last_name, address, metro_search, metro_full, phone, date, period_text, color,
                   comment):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro_search, metro_full)
        self.set_phone(phone)
        self.click_next_button()
        self.set_date(date)
        self.set_period(period_text)
        self.set_color(color)
        self.set_comment(comment)
        self.click_order_button()
        self.click_confirmation_button()

    @allure.step("Проверить появления окно с сообщением об успешном создании заказа")
    def check_confirmation_window(self):
        return self.wait_for_element(MakeOrderLocators.CHECK_STATUS_BUTTON)

    @allure.step("Клик по лого Самокат")
    def click_logo_samokat(self):
        self.click_on_element(MainPageLocators.LOGO_SAMOKAT)

    @allure.step("Проверить что лого самокат ведет на главную страницу")
    def logo_samokat_goto_mainpage(self):
        self.click_logo_samokat()
        return self.get_current_url()