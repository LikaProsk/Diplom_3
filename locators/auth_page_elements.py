from selenium.webdriver.common.by import By

element_email = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input")  # Поле ввода email
element_password = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input")  # Поле ввода пароля
button_access = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка "Войти"
button_registration = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
