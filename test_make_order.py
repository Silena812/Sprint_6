import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helper import generate_user_data


@pytest.mark.parametrize("click_button_method", [
    "click_top_order_button",
    "click_low_order_button"
])
@allure.title("Позитивный сценарий создания заказа")
def test_make_order_valid_data_order_created(driver, click_button_method):
    mainpage = MainPage(driver)
    orderpage = OrderPage(driver)
    user_data = generate_user_data()

    getattr(mainpage, click_button_method)()

    orderpage.make_order(
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        address=user_data['address'],
        metro_search=user_data['metro_station_search'],
        metro_full=user_data['metro_station_full'],
        phone=user_data['phone'],
        date=user_data['date'],
        period_text=user_data['period_text'],
        color=user_data['color'],
        comment=user_data['comment']
    )

    assert orderpage.check_confirmation_window() is not None, "Окно с кнопкой 'Посмотреть статус' не появилось"

