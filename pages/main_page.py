from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    faq_questions = (By.CSS_SELECTOR, 'div.accordion__button[data-accordion-component="AccordionItemButton"]')
    faq_answers = (By.CSS_SELECTOR, 'div.accordion__panel')
    top_order_button = (By.CLASS_NAME, 'Button_Button__ra12g')
    low_order_button = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')

    def click_question(self, index):
        self.driver.find_elements(*self.faq_questions)[index].click()

    def get_answer_text(self, index):
        return self.driver.find_elements(*self.faq_answers)[index].text

    def click_top_order_button(self):
        self.driver.find_elements(*self.top_order_button).click()

    def click_low_order_button(self):
        self.driver.find_elements(*self.low_order_button).click()

