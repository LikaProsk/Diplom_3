import allure

from locators.authoraize_home_page_elements import make_order_button
from page_object.home_page import HomePage


class AuthorizedHomePage(HomePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка отображения кнопки Соберите бургер')
    def check_visible_make_order_button(self, is_visible: bool = True):
        result = self._check_exists(make_order_button)

        assert result == is_visible

    @allure.step('Нажатие на кнопку Соберите бургер')
    def click_make_order_button(self):
        self._click_element(make_order_button)
