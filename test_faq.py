import pytest
import allure
from pages.main_page import MainPage
from data import Accordeon


@allure.title("Тест текста ответов в разделе Вопросы о важном")
@pytest.mark.parametrize('question_number, expected_text', Accordeon.faq_answers)
def test_faq_answers(driver, question_number, expected_text):
    page = MainPage(driver)

    with allure.step(f"Кликнуть на вопрос №{question_number}"):
        page.click_on_question(question_number)

    with allure.step(f"Проверить текст ответа на вопрос №{question_number}"):
        answer_locator = page.get_answer_locator_by_index(question_number)
        actual_text = page.get_text_on_element(answer_locator)
        assert expected_text == actual_text, f"Ожидалось: '{expected_text}', получено: '{actual_text}'"