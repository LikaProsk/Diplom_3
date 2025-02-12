from selenium.webdriver.common.by import By

order_history_button = (By.XPATH, '//a[contains(text(), "История заказов")]')  # Кнопка  "История заказов"
logout_button = (By.XPATH, "//button[contains(text(), 'Выход')]")  # Кнопка  "Выход"
user_name = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input")  # Поле "Имя"
user_email = (By.XPATH, "//label[contains(text(),'Логин')]/following-sibling::input")  # Поле "Логин"
