from selenium.webdriver.common.by import By

class MakeOrderLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_OPTIONS = (By.CLASS_NAME, "select-search__option")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_CHECKBOX_TEMPLATE = "//input[@id='{}']/.."
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(),'Заказать')])[2]")
    CONFIRMATION_BUTTON = (By.XPATH, "//button[text()='Да']")
    CANCELLATION_BUTTON = (By.XPATH, "//button[text()='Нет']")
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
