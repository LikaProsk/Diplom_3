import allure

from data import forgot_password_data
from locators.forgot_password_page_elements import email_field, restore_button
from page_object.base_class import BaseClass

from urls.site_urls import FORGOT_PASSWORD_PAGE_URL


class ForgotPasswordPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы для восстановления пароля')
    def open_forgot_password_page(self):
        self._open_page(FORGOT_PASSWORD_PAGE_URL)
        self._is_element_displayed(email_field)

    @allure.step('Заполнение поля email')
    def send_keys_email_field(self):
        self._send_keys(email_field, forgot_password_data.restore_email)

    @allure.step('Нажатие кнопки восстановления пароля')
    def click_restore_button(self):
        self._click_element(restore_button)
