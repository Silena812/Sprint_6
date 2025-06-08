import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_user_data


def test_make_order_top_order_button_valid_data_order_created(driver):
    mainpage = MainPage(driver)
    orderpage = OrderPage(driver)
    user_data = generate_user_data()
    mainpage.click_top_order_button()
    orderpage.make_order(
        name=user_data['first_name'],
        last_name=user_data['last_name'],
        address=user_data['address'],
        metro_search=user_data['metro_station_search'],  # первые 4 символа для поиска
        metro_full=user_data['metro_station_full'],  # полное название станции
        phone=user_data['phone'],
        date=user_data['date'],
        period_text=user_data['period_text'],
        color=user_data['color'],
        comment=user_data['comment']
    )
    assert WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(OrderPage.check_status_button)
    )