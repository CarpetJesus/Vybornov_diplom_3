from selenium.common.exceptions import StaleElementReferenceException
from pages.base_page import BasePage
from locators.page_locators import Locators
from curl import *
import allure

class OrderPage(BasePage):

    @allure.step("Получение общего числа выполненных заказов")
    def get_total_order_count(self):
        return int(self.get_text(Locators.ORDER_TOTAL_COUNT))

    @allure.step("Получение числа заказов, выполненных сегодня")
    def get_today_order_count(self):
        return int(self.get_text(Locators.ORDER_TODAY_COUNT))

    @allure.step("Проверка наличия заказа {order_number} в разделе 'В работе'")
    def is_order_in_work(self, order_number):
        orders = self.find_elements(Locators.ORDER_IN_WORK)
        order_number = int(order_number)

        return any(int(order.text) == order_number for order in orders)

    @allure.step("Переход на главную страницу")
    def go_to_main_page(self):
        self.click(Locators.CONSTRUCTOR_BUTTON)
        self.wait_for_url_contains(main_site)