from selenium.webdriver.common.by import By

button_personal_account = (By.XPATH, "//a//p[contains(text(), 'Личный Кабинет')]")  # Кнопка "Личный Кабинет"
button_account_access = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт"
element_make_burger = (By.XPATH, "//h1")  # Заголовок "Соберите бургер"
constructor_button = (By.LINK_TEXT, "Конструктор")  # Кнопка "Конструктор"
logo_element = (By.XPATH, "//a[@href='/']")  # Логотип "Stellar Burgers"
sauce_section_element = (By.XPATH, "//span[contains(text(), 'Соусы')]")  # Раздел "Соусы"
bun_section_element = (By.XPATH, "//span[contains(text(), 'Булки')]")  # Раздел "Булки"
stuffing_section_element = (By.XPATH, "//span[contains(text(), 'Начинки')]")  # Раздел "Начинки"
text_bun_section = (By.XPATH, f"//h2[contains(text(), 'Булки')]")  # Текст раздела "Булки"
text_sauce_section = (By.XPATH, f"//h2[contains(text(), 'Соусы')]")  # Текст раздела "Соусы"
text_stuffing_section = (By.XPATH, f"//h2[contains(text(), 'Начинки')]")  # Текст раздела "Начинки"
order_feed_button = (By.XPATH, "//a//p[contains(text(), 'Лента Заказов')]")  # Кнопка "Лента заказов"
ingredients = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")  # Раздел "Соберите бургер"
ingredient_details = (
By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified")]')  # Ингредиенты раздела "Соберите бургер"
close_ingredient_details_button = (
By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]')  # Кнопка закрытия раздел "Соберите бургер"
basket = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]//span")  # Корзина
bun = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]/parent::a")  # Булка "Флюоресцентная булка R2-D3"
meat = (By.XPATH,
        "//p[contains(text(), 'Мясо бессмертных моллюсков Protostomia')]/parent::a")  # Начинка "Мясо бессметрных моллюсков"
bun_count = (
By.XPATH, '//p[contains(text(), "Флюоресцентная булка R2-D3")]/parent::a//p[contains(@class, "counter_counter__num")]')
close_order_button = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button')  # Кнопка закрытия заказа
number_order = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')  # Номер заказа
