from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
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

    @allure.step("Переход на главную страницу")
    def go_to_main_page(self):
        self.click(Locators.CONSTRUCTOR_BUTTON)
        self.wait_for_url_contains(main_site)

    @allure.step("Получение номера первого заказа в ленте заказов")
    def get_first_order_number_in_feed(self):
        element = self.wait.until(
            EC.presence_of_element_located(Locators.FIRST_ORDER_NUMBER_IN_FEED)
        )
        return element.text.replace("#", "").strip()

    @allure.step("Проверка, что заказ {order_number} появился в 'В работе'")
    def is_order_in_work(self, order_number):
        order_number_modal = int(order_number)

        # Ждём появления хотя бы одного заказа в ленте
        self.wait.until(
            EC.presence_of_element_located(Locators.FIRST_ORDER_NUMBER_IN_FEED)
        )

        # Ждём, пока первый элемент в ленте станет нашим заказом
        self.wait.until(
            lambda driver: int(self.get_first_order_number_in_feed()) == order_number_modal
        )

        # Проверяем наличие заказа в разделе "В работе"
        orders_in_work_elements = self.find_elements(Locators.ORDER_IN_WORK)
        orders_in_work = []
        for o in orders_in_work_elements:
            text = o.text.strip()
            if text.isdigit():
                orders_in_work.append(int(text))

        return order_number_modal in orders_in_work



