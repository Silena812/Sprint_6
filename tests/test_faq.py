import pytest
import allure
from pages.main_page import MainPage
from data import Accordeon

class TestFAQ:

    @allure.title("Тест текста ответов в разделе Вопросы о важном")
    @allure.description("Тест кликает по-порядку на вопрос, получает текст ответа и сравнивает его с ожидаемым")
    @pytest.mark.parametrize('question_number, expected_text', Accordeon.faq_answers)
    def test_faq_answers(self, driver, question_number, expected_text):
        mainpage = MainPage(driver)
        mainpage.scroll_to_faq()
        mainpage.wait_for_faq_questions(question_number)
        mainpage.click_question(question_number)
        mainpage.wait_for_faq_answer(question_number)
        assert mainpage.get_text_faq_answer(question_number) == expected_text




