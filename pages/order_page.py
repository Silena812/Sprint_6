from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    last_name = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    address = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    metro = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро]')
    phone = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер]')
    next_button = (By.XPATH, "//button[text()='Далее']")

    def set_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    def set_metro(self, ):
        self.driver.find_element(*self.metro).send_keys(name)

    def set_phone(self, phone):
        self.driver.find_element(*self.phone).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def add_personal_data(self, name, last_name, address, metro, phone):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro()
        self.set_phone(phone)
        self.click_next_button()