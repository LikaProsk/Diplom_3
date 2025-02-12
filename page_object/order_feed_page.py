import random

import allure

from data.order_feed_data import structure
from locators.order_feed_elements import (orders_element, structure_element, number_completed_all_time_element,
                                          number_completed_for_today_element, close_order_details_button,
                                          orders_in_progress)
from locators.order_history_page_elements import order_history_list_id
from page_object.base_class import BaseClass
from urls.site_urls import ORDER_FEED_PAGE_URL


class OrderFeedPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открытие Ленты заказов')
    def open_order_feed_page(self):
        self._open_page(ORDER_FEED_PAGE_URL)

    @allure.step('Проверка открытой страницы')
    def check_open_order_feed_page(self):
        self._check_open_page(ORDER_FEED_PAGE_URL)

    @allure.step('Выбор заказ')
    def click_random_order(self):
        self._check_element_visibility_and_wait(orders_element)
        orders = self._get_elements(orders_element)
        orders[random.randint(0, len(orders) - 1)].click()

    @allure.step('Проверка выбранного заказа')
    def check_open_order_details(self):
        text = self._get_element_text(structure_element)
        assert text == structure

    @allure.step('Закрытие выбранного заказа')
    def closed_order_details(self):
        self._move_element_and_click(close_order_details_button)

    @allure.step('Получение количества заказов за все время')
    def get_number_completed_all_time(self):
        return int(self._get_element_text(number_completed_all_time_element))

    @allure.step('Получение количества заказов за сегодня')
    def get_number_completed_for_today(self):
        return int(self._get_element_text_and_wait(number_completed_for_today_element))

    @allure.step('Проверка увеличения количества закрытых заказов за все время')
    def check_closed_orders_quantity_increase_for_all_time(self, old_number_completed_all_time: int):
        result = self.get_number_completed_all_time()

        assert result > old_number_completed_all_time

    @allure.step('Проверка увеличения количества закрытых заказов за сегодня')
    def check_closed_orders_quantity_increase_for_today(self, old_number_completed_for_today: int):
        result = self.get_number_completed_for_today()

        assert result > old_number_completed_for_today

    @allure.step('Открытие заказов В работе')
    def check_open_in_progress_page(self, number_order: int):
        is_find = False

        result = self._get_elements(orders_in_progress)

        for order in result:
            id = order.text

            if str(number_order) in id:
                is_find = True

        assert is_find, "Заказ не найден"

    @allure.step('Проверка наличия заказов у пользователя')
    def check_user_orders_exist(self, order_history_ids: list):
        order_history_list = self._get_elements(order_history_list_id)
        ids = [order.text for order in order_history_list]
        result = list(set(order_history_ids) - set(ids))

        assert len(result) == 0
