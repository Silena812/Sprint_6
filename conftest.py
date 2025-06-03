import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.headless = False
    service = Service()
    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1200, 900)
    driver.get(main_site)
    try:
        close_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        close_btn.click()
        # Ждём, пока баннер исчезнет
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "App_CookieConsent__1yUIN"))
        )
    except Exception:
        pass
    yield driver
    driver.quit()