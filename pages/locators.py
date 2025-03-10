from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_SEE_BASKET = (By.CSS_SELECTOR, "div.basket-mini>span>a.btn[href*='basket']")

class MainPageLocators():
    pass

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner>p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_ITEM_IN_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(1)  strong")
    OFFER= (By.CSS_SELECTOR, "div#messages div.alert:nth-child(2)  strong")
    SUMM_BASKET = (By.CSS_SELECTOR, "div#messages div.alert:nth-child(3)  strong")
    PRICE_ITEM = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    NAME_ITEM = (By.CSS_SELECTOR, "div.product_main > h1")