from selenium.webdriver.common.by import By

password_field = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")  # Поле ввода пароля
div_password_field = (
By.XPATH, "//label[contains(text(),'Пароль')]/parent::div[contains(@class, 'input')]")  # Активное поле ввода пароля
active_class = "input_status_active"  # Активация поля ввода пароля
show_hide_password_button = (
By.XPATH, '//div[@class="input__container"]//div[contains(@class, "input__icon")]')  # Кнопка показа и скрытия пароля
restore_password_text_section = (By.XPATH, f"//h2[contains(text(), 'Восстановление пароля')]")  # Восстановление пароля
