from selenium.webdriver.common.by import By

orders_element = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]//a")  # Вкладка "Лента заказов"
structure_element = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]//p[contains(text(), 'Cостав')]")  # Cостав
number_completed_all_time_element = (By.XPATH,
                                     "//div[contains(@class, 'OrderFeed_ordersData')]//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")  # Выполнено за все время
number_completed_for_today_element = (By.XPATH,
                                      "//div[contains(@class, 'OrderFeed_ordersData')]//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")  # Выполнено за сегодня
close_order_details_button = (By.XPATH,
                              '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "Modal_modal__close_modified")]')  # Кнопка закрытия деталей заказа
orders_in_progress = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderList_")]//li')  # Заказы в работе
order_history_list_id = (By.XPATH,
                         '//li[contains(@class, "OrderHistory_listItem")]/a/div/p[contains(@class, "text_type_digits-default")]')  # История заказов
