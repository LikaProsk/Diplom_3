import allure

from page_object.auth_page import AuthPage
from page_object.authorized_home_page import AuthorizedHomePage
from page_object.home_page import HomePage
from page_object.order_feed_page import OrderFeedPage


class TestMainFunctionality:

    @allure.title('Проверка основного функционала незалогиненным пользователем')
    @allure.description('Для проверки незалогиенным пользователем кликаем  на Ленту заказов, ингредиент с деталями, '
                        'закрываем окно с деталями, добавляем ингредиент в заказ и  увеличиваем его каунтер')
    def test_main_functionality_not_authorized(self, driver):
        home_page_object = HomePage(driver)
        order_feed_page_object = OrderFeedPage(driver)
        authorized_home_page_object = AuthorizedHomePage(driver)

        home_page_object.open_home_page()
        home_page_object.check_open_home_page()
        home_page_object.click_order_feed_button()
        order_feed_page_object.check_open_order_feed_page()
        home_page_object.click_designer_button()
        home_page_object.check_element_make_burger()
        home_page_object.click_random_ingredient()
        home_page_object.check_ingredient_details_element()
        home_page_object.close_ingredient_details()
        home_page_object.add_bun_ingredient_to_basket()
        home_page_object.check_bun_count(2)
        authorized_home_page_object.check_visible_make_order_button(False)

    @allure.title('Проверка основного функционала залогиненным пользователем')
    @allure.description('Для проверки залогиненным пользователем кликаем  на Ленту заказов, ингредиент с деталями, '
                        'закрываем окно с деталями, добавляем ингредиент в заказ и  увеличиваем его каунтер')
    def test_main_functionality_authorized(self, driver, create_user):
        home_page_object = HomePage(driver)
        order_feed_page_object = OrderFeedPage(driver)
        authorized_home_page_object = AuthorizedHomePage(driver)
        auth_page_object = AuthPage(driver)

        home_page_object.open_home_page()
        home_page_object.check_open_home_page()
        home_page_object.click_button_account_access()
        auth_page_object.check_auth_page()
        auth_page_object.send_keys_email_field(create_user.get("email"))
        auth_page_object.send_keys_password_field(create_user.get("password"))
        auth_page_object.click_access_button()
        home_page_object.check_open_home_page()
        home_page_object.click_order_feed_button()
        order_feed_page_object.check_open_order_feed_page()
        home_page_object.click_designer_button()
        home_page_object.check_element_make_burger()
        home_page_object.click_random_ingredient()
        home_page_object.check_ingredient_details_element()
        home_page_object.close_ingredient_details()
        home_page_object.add_bun_ingredient_to_basket()
        home_page_object.check_bun_count(2)
        authorized_home_page_object.check_visible_make_order_button()
