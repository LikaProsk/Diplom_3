from selenium.webdriver.common.by import By

email_field = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле ввода email
restore_button = (By.XPATH, "//button[contains(text(), 'Восстановить')]")  # Кнопка "Восстановить"
