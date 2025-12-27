from pages.base_page import BasePage
from locators.page_locators import Locators
from curl import *

class MainPage(BasePage):

    def go_to_constructor(self):
        self.click(Locators.CONSTRUCTOR_BUTTON)
        self.wait_for_url(main_site)

    def go_to_order_feed(self):
        self.click(Locators.ORDER_FEED_BUTTON)
        self.wait_for_url_contains("/feed")

    def click_ingredient(self):
        self.click(Locators.INGREDIENT_CARD)
        self.find_element(Locators.INGREDIENT_WINDOW_MODAL_TITLE)

    def close_ingredient_modal(self):
        self.click(Locators.INGREDIENT_WINDOW_MODAL_CLOSE)
        self.wait_for_invisible(Locators.INGREDIENT_WINDOW_MODAL_TITLE)

    def get_constructor_text(self):
        return self.get_text(Locators.CONSTRUCTOR_TEXT)

    def is_ingredient_modal_opened(self):
        return self.is_visible(Locators.INGREDIENT_WINDOW_MODAL_TITLE)

    def add_ingredient_to_constructor(self):
        ingredient = self.find_element(Locators.INGREDIENT_CARD)
        drop_place = self.find_element(Locators.INGREDIENT_PLACE_TO_DROP)
        self.drag_and_drop(ingredient, drop_place)

    def get_ingredient_counter(self):
        counter = self.find_element(Locators.INGREDIENT_WINDOW_MODAL_COUNT)
        return int(counter.text)
