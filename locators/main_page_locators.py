from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_SECTION = (By.CLASS_NAME, 'Home_FAQ__3uVm4')
    FAQ_QUESTIONS = {
        1: (By.XPATH, '//*[@id="accordion__heading-0"]/parent::div'),
        2: (By.XPATH, '//*[@id="accordion__heading-1"]/parent::div'),
        3: (By.XPATH, '//*[@id="accordion__heading-2"]/parent::div'),
        4: (By.XPATH, '//*[@id="accordion__heading-3"]/parent::div'),
        5: (By.XPATH, '//*[@id="accordion__heading-4"]/parent::div'),
        6: (By.XPATH, '//*[@id="accordion__heading-5"]/parent::div'),
        7: (By.XPATH, '//*[@id="accordion__heading-6"]/parent::div'),
        8: (By.XPATH, '//*[@id="accordion__heading-7"]/parent::div')
    }

    FAQ_ANSWERS = {
        1: (By.XPATH, '//*[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//*[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//*[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//*[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//*[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//*[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//*[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//*[@id="accordion__panel-7"]')
    }


    TOP_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    LOW_ORDER_BUTTON = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')

    LOGO_YANDEX = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    LOGO_SAMOKAT = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    COOKIE_CLOSE_BUTTON = (By.ID, "rcc-confirm-button")
    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")

