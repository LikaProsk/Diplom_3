import allure

from page_object.auth_page import AuthPage
from page_object.authorized_home_page import AuthorizedHomePage
from page_object.home_page import HomePage
from page_object.order_feed_page import OrderFeedPage
from page_object.personal_account_page import PersonalAccountPage


class TestOrderFeed:

    @allure.title('Проверка раздела Лента заказов')
    @allure.description(' Для проверки кликаем  на заказ, открываем окно с деталями, смотрим Историю заказов  на '
                        'странице Ленты заказов, создаем новый заказ, следим за увеличением счётчиков '
                        'Выполнено за все время и за сегодня , за появлением номера заказа в разделе В работе')
    def test_order_feed(self, driver, create_user):
        home_page_object = HomePage(driver)
        auth_page_object = AuthPage(driver)
        order_feed_page_object = OrderFeedPage(driver)
        authorized_home_page_object = AuthorizedHomePage(driver)
        personal_account_page_object = PersonalAccountPage(driver)

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
        order_feed_page_object.click_random_order()
        order_feed_page_object.check_open_order_details()
        order_feed_page_object.closed_order_details()
        number_completed_all_time = order_feed_page_object.get_number_completed_all_time()
        number_completed_for_today = order_feed_page_object.get_number_completed_for_today()
        home_page_object.click_designer_button()
        home_page_object.check_element_make_burger()
        home_page_object.add_bun_ingredient_to_basket()
        home_page_object.add_meat_ingredient_to_basket()
        authorized_home_page_object.check_visible_make_order_button()
        authorized_home_page_object.click_make_order_button()
        number_order = home_page_object.get_number_order()
        home_page_object.click_close_order_button()
        home_page_object.click_order_feed_button()
        order_feed_page_object.check_open_order_feed_page()
        order_feed_page_object.check_open_in_progress_page(number_order)
        order_feed_page_object.check_closed_orders_quantity_increase_for_all_time(number_completed_all_time)
        order_feed_page_object.check_closed_orders_quantity_increase_for_today(number_completed_for_today)
        home_page_object.click_personal_account_button()
        personal_account_page_object.check_personal_account_page()
        personal_account_page_object.click_order_history_button()
        order_history_list_id = personal_account_page_object.get_order_history_list_id()
        home_page_object.click_order_feed_button()
        order_feed_page_object.check_open_order_feed_page()
        order_feed_page_object.check_user_orders_exist(order_history_list_id)
