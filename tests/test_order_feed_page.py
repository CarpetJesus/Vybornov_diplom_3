import allure
from pages.order_page import OrderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import Credentials
from curl import *

class TestOrderFeedPage:

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после нового заказа")
    def test_total_orders_count(self, driver):
        feed_page = OrderPage(driver)
        feed_page.open_page(order_feed)

        total_before = feed_page.get_total_order_count()

        login_page = LoginPage(driver)
        login_page.open_page(login_site)
        login_page.login(Credentials.email, Credentials.password)

        main_page = MainPage(driver)
        main_page.make_order()
        main_page.get_order_number()
        main_page.close_confirm_window()

        feed_page.open_page(order_feed)
        total_after = feed_page.get_total_order_count()

        assert total_after == total_before + 1

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_in_work(self, login_and_create_order):
        driver, order_number = login_and_create_order

        feed_page = OrderPage(driver)
        feed_page.open_page(order_feed)

        assert feed_page.is_order_in_work(order_number)

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после нового заказа")
    def test_today_orders_count(self, driver):
        feed_page = OrderPage(driver)
        feed_page.open_page(order_feed)

        today_before = feed_page.get_today_order_count()

        login_page = LoginPage(driver)
        login_page.open_page(login_site)
        login_page.login(Credentials.email, Credentials.password)

        main_page = MainPage(driver)
        main_page.make_order()
        main_page.get_order_number()
        main_page.close_confirm_window()

        feed_page.open_page(order_feed)
        today_after = feed_page.get_today_order_count()

        assert today_after == today_before + 1
