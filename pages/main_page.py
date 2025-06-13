import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators



class MainPage(BasePage):

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

    @allure.step("Прокрутить до секции Вопросы о важном")
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Подождать появления вопроса по номеру {data}")
    def wait_for_faq_questions(self, data):
        self.wait_for_element(MainPageLocators.FAQ_QUESTIONS[data])

    @allure.step("Клик на вопрос по номеру {data}")
    def click_question(self, data):
        self.click_on_element(MainPageLocators.FAQ_QUESTIONS[data])

    @allure.step("Подождать появления ответа по номеру {data}")
    def wait_for_faq_answer(self, data):
        self.wait_for_element(MainPageLocators.FAQ_ANSWERS[data])

    @allure.step("Получить текст ответа по номеру {data}")
    def get_text_faq_answer(self, data):
        return self.get_text_on_element(MainPageLocators.FAQ_ANSWERS[data])

    #@allure.step("Подождать появление нужного номера вопроса")
    #def wait_for_faq(self,question_number):
        #self.wait_for_element(MainPageLocators.FAQ_QUESTIONS[question_number])

    #@allure.step("Подождать появление нужного номера ответа")
    #def wait_for_faq_answer(self, question_number):
        #self.wait_for_element(MainPageLocators.FAQ_ANSWERS[question_number])

    #@allure.step("Получить текст ответа")
    #def get_text_faq_answer(self, question_number):
        #self.get_text_on_element(MainPageLocators.FAQ_ANSWERS[question_number])

    #def click_faq_question(self, index):
        # questions = self.driver.find_elements(*MainPageLocators.FAQ_QUESTIONS)
    #  questions[index].click()

        #  def wait_for_faq_answer(self, index):
    #    questions = self.driver.find_elements(*MainPageLocators.FAQ_QUESTIONS)
        #      aria_controls = questions[index].get_attribute("aria-controls")
        #     self.wait.until(EC.visibility_of_element_located((By.ID, aria_controls)))

        #  def get_faq_answer_text(self, index):
        #    questions = self.driver.find_elements(*MainPageLocators.FAQ_QUESTIONS)
        #       answer_id = questions[index].get_attribute("aria-controls")
        #   answer = self.driver.find_element(By.ID, answer_id)
    #   return answer.text

