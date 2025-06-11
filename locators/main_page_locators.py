from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_QUESTIONS = (By.CSS_SELECTOR, 'div.accordion__button[data-accordion-component="AccordionItemButton"]')
    FAQ_ANSWERS = (By.CSS_SELECTOR, 'div.accordion__panel')

    TOP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    LOW_ORDER_BUTTON = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')

    LOGO_YANDEX = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    LOGO_SAMOKAT = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    @staticmethod
    def get_question_by_index(self, index):
        return self.find_elements(MainPageLocators.FAQ_QUESTIONS)[index - 1]

    @staticmethod
    def get_answer_by_index(self, index):
        return self.find_elements(MainPageLocators.FAQ_ANSWERS)[index - 1]