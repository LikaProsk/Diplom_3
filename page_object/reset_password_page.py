import allure

from locators.reset_password_page_elements import restore_password_text_section, show_hide_password_button, \
    div_password_field, active_class
from page_object.base_class import BaseClass
from urls.site_urls import RESET_PASSWORD_PAGE_URL


class ResetPasswordPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы восстановления пароля')
    def open_reset_password_page(self):
        self._open_page(RESET_PASSWORD_PAGE_URL)
        self._is_element_displayed(restore_password_text_section)

    @allure.step('Проверка редиректа на страницу восстановления пароля')
    def check_redirect_to_password_reset_page(self):
        self._check_open_page(RESET_PASSWORD_PAGE_URL)

    @allure.step('Нажатие кнопки скрытия и показа пароля')
    def click_show_hide_password_button(self):
        self._click_element(show_hide_password_button)

    @allure.step('Проверка подсвечивания поля ввода пароля')
    def check_password_field_is_active(self):
        class_attribute_value = self._get_element_attribute(div_password_field, "class")
        assert active_class in class_attribute_value
