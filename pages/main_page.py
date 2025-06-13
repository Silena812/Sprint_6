import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators



class MainPage(BasePage):

    @allure.step("Клик на вопрос")
    def click_question(self, index):
        self.click_on_element(MainPageLocators.FAQ_QUESTIONS)[index].click()

    @allure.step("Получить текст ответа")
    def get_answer_text(self, index):
        return self.get_text_on_element(MainPageLocators.FAQ_ANSWERS)[index].text

    @allure.step("Клик на верхнюю кнопку Заказать")
    def click_top_order_button(self):
        self.click_on_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Клик на нижнюю кнопку Заказать")
    def click_low_order_button(self):
        self.click_on_element(MainPageLocators.LOW_ORDER_BUTTON)

    @allure.step("Клик по лого Яндекс")
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Проверить что лого яндекса ведет на страницу Дзен")
    def logo_yandex_goto_dzen(self):
        self.click_logo_yandex()
        self.switch_window()
        self.wait_for_url_contains("dzen.ru")
        return self.get_current_url()

