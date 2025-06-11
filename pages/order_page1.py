from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrderPage1:
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

    logo_yandex = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    logo_samokat = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self,first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    def set_last_name(self,last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def set_address(self,address):
        self.driver.find_element(*self.address).send_keys(address)


    def set_metro(self, metro_search, metro_partial):
        metro_input = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.metro_input)
        )
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro_search)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.metro_options)
        )

        for option in self.driver.find_elements(*self.metro_options):
            if metro_partial in option.text:
                option.click()
                break

    def set_phone(self,phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_date(self,date):
        self.driver.find_element(*self.date).send_keys(date)
        self.driver.find_element(*self.date).send_keys(Keys.ENTER)

    def set_period(self, period_text):
        self.driver.find_element(*self.period_dropdown).click()
        period_options = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.period_options)
        )
        for option in period_options:
            if period_text == option.text:
                option.click()
                break

    def set_color(self, color):
        xpath = self.color_checkbox_template.format(color)
        self.driver.find_element(By.XPATH, xpath).click()

    def set_comment(self,comment):
        self.driver.find_element(*self.comment).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_confirmation_button(self):
        self.driver.find_element(*self.confirmation_button).click()

    def make_order(self, first_name, last_name, address, metro_search, metro_full, phone, date, period_text, color, comment):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(metro_search, metro_full)
        self.set_phone(phone)
        self.click_next_button()
        self.set_date(date)
        self.set_period(period_text)
        self.set_color(color)
        self.set_comment(comment)
        self.click_order_button()
        self.click_confirmation_button()


    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    def click_logo_samokat(self):
        self.driver.find_element(*self.logo_samokat).click()