import allure

from page_object.forgot_password_page import ForgotPasswordPage
from page_object.reset_password_page import ResetPasswordPage


class TestRestorePassword:

    @allure.title('Проверка Восстановления пароля')
    @allure.description(' Для проверки  переходим на страницу восстановления пароля , кликаем  «Восстановить пароль», '
                        'вводим email , кликаем  «Восстановить»,кликаем показать/скрыть пароль, '
                        'смотрим , что поле активно')
    def test_restore_password(self, driver):
        forgot_password_page_object = ForgotPasswordPage(driver)
        forgot_password_page_object.open_forgot_password_page()
        forgot_password_page_object.send_keys_email_field()
        forgot_password_page_object.click_restore_button()
        reset_password_page_object = ResetPasswordPage(driver)
        reset_password_page_object.check_redirect_to_password_reset_page()
        reset_password_page_object.click_show_hide_password_button()
        reset_password_page_object.check_password_field_is_active()
