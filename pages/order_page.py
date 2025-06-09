from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    # Локаторы для полей формы заказа
    first_name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_input_locator = (By.CLASS_NAME, "select-search__input")
    metro_options_locator = (By.CLASS_NAME, "select-search__option")
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    period_dropdown = (By.CLASS_NAME, "Dropdown-control")
    period_options_locator = (By.CLASS_NAME, "Dropdown-option")
    color_checkbox_template = "//input[@id='{}']/.."
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g') and contains(text(),'Заказать')])[2]")
    confirmation_button = (By.XPATH, "//button[text()='Да']")
    cancelation_button = (By.XPATH, "//button[text()='Нет']")
    check_status_button = (By.XPATH, "//button[text()='Посмотреть статус']")

    logo_yandex = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    logo_samokat = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    def __init__(self, driver):
        self.driver = driver

    def set_metro(self, metro_search, metro_partial):
        metro_input = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.metro_input_locator)
        )
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro_search)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.metro_options_locator)
        )

        options = self.driver.find_elements(*self.metro_options_locator)
        for option in options:
            if metro_partial in option.text:
                option.click()
                return
        raise Exception(f"Станция метро с текстом '{metro_partial}' не найдена")

    def make_order(self, name, last_name, address, metro_search, metro_full, phone, date, period_text, color, comment):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.first_name_input)
        ).send_keys(name)

        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.address_input).send_keys(address)

        self.set_metro(metro_search, metro_full)

        self.driver.find_element(*self.phone_input).send_keys(phone)

        self.driver.find_element(*self.next_button).click()

        wait = WebDriverWait(self.driver, 10)
        date_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='* Когда привезти самокат']"))
        )
        date_element.send_keys(date + "\n")
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.click()

        # Выбор периода аренды
        self.driver.find_element(*self.period_dropdown).click()
        period_options = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.period_options_locator)
        )
        for option in period_options:
            if period_text == option.text:
                option.click()
                break

        # Выбор цвета

        self.driver.find_element(By.XPATH, f'//label[contains(., "{color}")]').click()

        self.driver.find_element(*self.comment_input).send_keys(comment)

        # Нажать кнопку "Заказать"
        self.driver.find_element(*self.order_button).click()

        self.driver.find_element(*self.confirmation_button).click()


    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    def click_logo_samokat(self):
        self.driver.find_element(*self.logo_samokat).click()