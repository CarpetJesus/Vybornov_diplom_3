import allure
from pages.base_page import BasePage
from locators.page_locators import Locators

class LoginPage(BasePage):

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        email_field = self.find_element(Locators.EMAIL_LOG)
        email_field.clear()
        email_field.send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        password_field = self.find_element(Locators.PASSWORD_LOG)
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Нажатие кнопки 'Войти'")
    def click_login_button(self):
        self.click(Locators.LOG_BUTTON)

    @allure.step("Логин пользователя: {email}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
