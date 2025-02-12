import random
from time import sleep

import allure

from data.home_page_data import make_burger, text_ingredient_details
from locators.home_page_elements import button_personal_account, constructor_button, order_feed_button, \
    element_make_burger, ingredients, ingredient_details, close_ingredient_details_button, bun, basket, bun_count, \
    button_account_access, meat, number_order, close_order_button
from page_object.base_class import BaseClass
from urls.site_urls import HOME_PAGE_URL


class HomePage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие главной страницы')
    def open_home_page(self):
        self._open_page(HOME_PAGE_URL)

    @allure.step('Проверка открытой страницы')
    def check_open_home_page(self):
        self._check_open_page(HOME_PAGE_URL)

    @allure.step('Нажатие кнопки Личный кабинет')
    def click_personal_account_button(self):
        self._move_element_and_click(button_personal_account)

    @allure.step('Нажатие кнопки Соберите бургер')
    def click_designer_button(self):
        self._click_element(constructor_button)

    @allure.step('Нажатие кнопки Лента заказов')
    def click_order_feed_button(self):
        self._move_element_and_click(order_feed_button)

    @allure.step('Проверка раздела Соберите бургер')
    def check_element_make_burger(self):
        text = self._get_element_text(element_make_burger)

        assert text == make_burger

    @allure.step('Нажатие на ингредиент')
    def click_random_ingredient(self):
        ingredients_elements = self._get_elements(ingredients)
        ingredients_elements[random.randint(0, len(ingredients_elements) - 1)].click()

    @allure.step('Проверка выбранного ингредиента')
    def check_ingredient_details_element(self):
        text = self._get_element_text(ingredient_details)

        assert text == text_ingredient_details

    @allure.step('Закрытие выбранного ингредиента')
    def close_ingredient_details(self):
        self._click_element(close_ingredient_details_button)

    @allure.step('Добавление булочки в корзину')
    def add_bun_ingredient_to_basket(self):
        self._move_to_element(bun)
        self._drag_and_drop(bun, basket)

    @allure.step('Добавление начинки в корзину')
    def add_meat_ingredient_to_basket(self):
        self._move_to_element(meat)
        self._drag_and_drop(meat, basket)

    @allure.step('Проверка количества булочек')
    def check_bun_count(self, count: int):
        sleep(5)
        text = self._get_element_text_and_wait(bun_count)
        assert int(text) == count

    @allure.step('Нажатие кнопки Личный кабинет')
    def click_button_account_access(self):
        self._click_element(button_account_access)

    @allure.step('Получение количества заказов')
    def get_number_order(self):
        result = 9999

        while result == 9999:
            number = int(self._get_element_text_and_wait(number_order))
            if number != 9999:
                result = number

        return result

    @allure.step('Нажатие кнопки закрытия заказа')
    def click_close_order_button(self):
        self._move_element_and_click(close_order_button)
