import allure

from locators.personal_account_page_elements import logout_button
from page_object.base_class import BaseClass
from urls.site_urls import ORDER_HISTORY_URL


class OrderHistoryPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы  История заказов')
    def open_order_history_page(self):
        self._open_page(ORDER_HISTORY_URL)

    @allure.step('Проверка открытой страницы')
    def check_order_history_page(self):
        self._check_open_page(ORDER_HISTORY_URL)

    @allure.step('Нажатие кнопки Выход')
    def click_logout_button(self):
        self._click_element(logout_button)
