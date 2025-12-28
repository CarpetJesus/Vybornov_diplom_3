import allure
from pages.main_page import MainPage
from curl import *

class TestMainPage:

    @allure.title("Переход по клику на конструктор")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)

        page.open_page(order_feed)

        page.go_to_constructor()

        burger_text = page.get_constructor_text()

        assert page.is_current_url(main_site)
        assert burger_text == "Соберите бургер"

    @allure.title("Переход по клику на ленту заказов")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)

        page.open_page(main_site)

        page.go_to_order_feed()

        assert page.is_current_url(order_feed)

    @allure.title("Открытие окна ингредиента с деталями")
    def test_open_ingredient_details(self, driver):
        page = MainPage(driver)

        page.open_page(main_site)

        page.click_ingredient()

        assert page.is_ingredient_modal_opened()

    @allure.title("Закрытие окна ингредиента с деталями по крестику")
    def test_close_ingredient_details(self, driver):
        page = MainPage(driver)

        page.open_page(main_site)

        page.click_ingredient()
        page.close_ingredient_modal()

        assert not page.is_ingredient_modal_opened()

    @allure.title("Увеличение счетчика ингредиента при добавлении в конструктор")
    def test_count_ingredient_to_constructor(self, driver):
        page = MainPage(driver)

        page.open_page(main_site)

        count_before = page.get_ingredient_counter()
        page.add_ingredient_to_constructor()
        count_after = page.get_ingredient_counter()

        assert count_after == count_before + 2
