from selenium.webdriver.common.by import By

order_history_list_id = (By.XPATH,
                         '//li[contains(@class, "OrderHistory_listItem")]/a/div/p[contains(@class, "text_type_digits-default")]')  # Номера заказов в истории заказов
