import allure

from locators.auth_page_elements import element_email, element_password, button_access
from page_object.base_class import BaseClass
from urls.site_urls import AUTH_URL


class AuthPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы авторизации')
    def open_auth_page(self):
        self._open_page(AUTH_URL)

    @allure.step('Проверка открытой страницы')
    def check_auth_page(self):
        self._check_element_visibility_and_wait(button_access)

    @allure.step('Заполнение поля email')
    def send_keys_email_field(self, email):
        self._send_keys(element_email, email)

    @allure.step('Заполнение поля пароля')
    def send_keys_password_field(self, password):
        self._send_keys(element_password, password)

    @allure.step('Нажатие кнопки Войти')
    def click_access_button(self):
        self._click_element(button_access)
