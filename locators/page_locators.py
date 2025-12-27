from selenium.webdriver.common.by import By

class Locators:

    #Главная страница

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/..")
    ORDER_FEED_BUTTON = (By.XPATH, "//header//a[@href='/feed']")
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']/..")
    CONSTRUCTOR_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT_CARD = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a[1]")

    INGREDIENT_WINDOW_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_WINDOW_MODAL_CLOSE = (By.XPATH, "//section[contains(@class,'Modal_modal__')]//button")

    INGREDIENT_PLACE_TO_DROP = (By.CSS_SELECTOR, ".constructor-element_pos_top")
    INGREDIENT_WINDOW_MODAL_COUNT = (
        By.XPATH,
        "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a[contains(@class,'BurgerIngredient_ingredient')]//p[contains(@class,'counter_counter__num')]"
    )

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    ORDER_CONFIRM_WINDOW_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    CREATED_ORDER_WINDOW_NUMBER_CONFIRM = (By.XPATH, "//h2[contains(@class,'digits-large mb-8')]")

    #Локаторы для логина
    EMAIL_LOG = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_LOG = (By.NAME, "Пароль")
    LOG_BUTTON = (By.XPATH, "//button[text()='Войти']")

    #Лента заказов
    FEED_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")

    ORDER_TOTAL_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDER_TODAY_COUNT = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_WORK = (
        By.XPATH, "//ul[contains(@class, 'orderListReady')]//li[contains(@class, 'text')]"
    )
    FIRST_ORDER_IN_LIST = (By.CSS_SELECTOR, ".OrderHistory_listItem")

    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class^='Modal_modal_overlay']")








