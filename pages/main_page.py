from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    FAQ_QUESTIONS = (By.CSS_SELECTOR, 'div.accordion__button[data-accordion-component="AccordionItemButton"]')
    FAQ_ANSWERS = (By.CSS_SELECTOR, 'div.accordion__panel')

    def click_question(self, index):
        self.driver.find_elements(*self.FAQ_QUESTIONS)[index].click()

    def get_answer_text(self, index):
        return self.driver.find_elements(*self.FAQ_ANSWERS)[index].text

