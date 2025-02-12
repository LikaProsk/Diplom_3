import allure

from locators.order_history_page_elements import order_history_list_id
from locators.personal_account_page_elements import order_history_button, user_name, user_email
from page_object.base_class import BaseClass
from urls.site_urls import ACC_PROFILE_PAGE


class PersonalAccountPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие страницы Личный кабинет')
    def open_personal_account_page(self):
        self._open_page(ACC_PROFILE_PAGE)

    @allure.step('Проверка открытой страницы')
    def check_personal_account_page(self):
        self._check_open_page(ACC_PROFILE_PAGE)

    @allure.step('Проверка имени пользователя')
    def check_user_name(self, name: str):
        personal_name = self._get_element_attribute(user_name, "value")
        assert personal_name == name

    @allure.step('Проверка email пользователя')
    def check_user_email(self, email: str):
        personal_email = self._get_element_attribute(user_email, "value")
        assert personal_email == email

    @allure.step('Проверка отображения кнопки История заказов')
    def check_order_history_button_visibility(self):
        self._check_element_visibility_and_wait(order_history_button)

    @allure.step('Нажатие кнопки История заказов')
    def click_order_history_button(self):
        self._move_element_and_click(order_history_button)

    @allure.step('Получения списка заказов в Истории заказов')
    def get_order_history_list_id(self):
        result = []
        number_of_attempts = 0
        while len(result) == 0 and number_of_attempts < 10:
            order_history_list = self._get_elements(order_history_list_id)
            result = [order.text for order in order_history_list]
            number_of_attempts += 1

        return result
