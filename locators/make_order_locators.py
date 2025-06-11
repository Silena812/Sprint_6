from selenium.webdriver.common.by import By

class MakeOrderLocators:
    first_name = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_input = (By.CLASS_NAME, "select-search__input")
    metro_options = (By.CLASS_NAME, "select-search__option")
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")
    date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    period_dropdown = (By.CLASS_NAME, "Dropdown-control")
    period_options = (By.CLASS_NAME, "Dropdown-option")
    color_checkbox_template = "//input[@id='{}']/.."
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(),'Заказать')])[2]")
    confirmation_button = (By.XPATH, "//button[text()='Да']")
    cancelation_button = (By.XPATH, "//button[text()='Нет']")
    check_status_button = (By.XPATH, "//button[text()='Посмотреть статус']")
