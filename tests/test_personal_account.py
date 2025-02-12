import allure

from page_object.auth_page import AuthPage
from page_object.home_page import HomePage
from page_object.order_history_page import OrderHistoryPage
from page_object.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка Личного кабинета')
    @allure.description(' Для проверки кликаем  «Личный кабинет», переходим в Историю заказов и выход')
    def test_personal_account(self, driver, create_user):
        auth_page_object = AuthPage(driver)
        home_page_object = HomePage(driver)
        order_history_page_object = OrderHistoryPage(driver)
        personal_account_page_object = PersonalAccountPage(driver)

        auth_page_object.open_auth_page()
        auth_page_object.check_auth_page()
        auth_page_object.send_keys_email_field(create_user.get("email"))
        auth_page_object.send_keys_password_field(create_user.get("password"))
        auth_page_object.click_access_button()
        home_page_object.check_open_home_page()
        home_page_object.click_personal_account_button()
        personal_account_page_object.check_personal_account_page()
        personal_account_page_object.check_user_name(create_user.get("name"))
        personal_account_page_object.check_user_email(create_user.get("email"))
        personal_account_page_object.check_order_history_button_visibility()
        personal_account_page_object.click_order_history_button()
        order_history_page_object.check_order_history_page()
        order_history_page_object.click_logout_button()
        auth_page_object.check_auth_page()
