import allure
from pages.base_page import BasePage
from locators.page_locators import Locators
from curl import *

class MainPage(BasePage):

    @allure.step("Переход на страницу конструктора")
    def go_to_constructor(self):
        self.wait_for_invisible(Locators.MODAL_OVERLAY)
        self.click(Locators.CONSTRUCTOR_BUTTON)
        self.wait_for_url(main_site)

    @allure.step("Переход на ленту заказов")
    def go_to_order_feed(self):
        self.click(Locators.ORDER_FEED_BUTTON)
        self.wait_for_url_contains("/feed")


    @allure.step("Закрытие окна подтверждения заказа")
    def close_confirm_window(self):
        self.click(Locators.ORDER_CONFIRM_WINDOW_CLOSE_BUTTON)
        self.wait_for_invisible(Locators.ORDER_CONFIRM_WINDOW_CLOSE_BUTTON)

    @allure.step("Открытие модального окна ингредиента")
    def click_ingredient(self):
        self.click(Locators.INGREDIENT_CARD)
        self.find_element(Locators.INGREDIENT_WINDOW_MODAL_TITLE)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_order_button(self):
        self.wait_for_invisible(Locators.MODAL_OVERLAY)
        self.click(Locators.PLACE_ORDER_BUTTON)

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click(Locators.INGREDIENT_WINDOW_MODAL_CLOSE)
        self.wait_for_invisible(Locators.INGREDIENT_WINDOW_MODAL_TITLE)

    @allure.step("Получение текста конструктора")
    def get_constructor_text(self):
        return self.get_text(Locators.CONSTRUCTOR_TEXT)

    @allure.step("Получение номера созданного заказа")
    def get_order_number(self):
        self.wait_for_order_number()
        return self.get_text(Locators.CREATED_ORDER_WINDOW_NUMBER_CONFIRM)

    @allure.step("Проверка, открыто ли окно ингредиента")
    def is_ingredient_modal_opened(self):
        return self.is_visible(Locators.INGREDIENT_WINDOW_MODAL_TITLE)

    @allure.step("Добавление ингредиента в конструктор")
    def add_ingredient_to_constructor(self):
        ingredient = self.find_element(Locators.INGREDIENT_CARD)
        drop_place = self.find_element(Locators.INGREDIENT_PLACE_TO_DROP)
        self.drag_and_drop(ingredient, drop_place)

    @allure.step("Получение значения счётчика ингредиента")
    def get_ingredient_counter(self):
        counter = self.find_element(Locators.INGREDIENT_WINDOW_MODAL_COUNT)
        return int(counter.text)

    @allure.step("Создание заказа")
    def make_order(self):
        self.find_element(Locators.CONSTRUCTOR_TEXT)
        self.wait_for_invisible(Locators.MODAL_OVERLAY)
        self.add_ingredient_to_constructor()
        self.click_order_button()

    def wait_for_order_number(self, timeout=10):
        def number_ready():
            text = self.get_text(Locators.CREATED_ORDER_WINDOW_NUMBER_CONFIRM)
            return text != "9999" and text.isdigit()

        self.wait.until(lambda _: number_ready())

