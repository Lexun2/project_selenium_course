from .locators import BasketPageLocators
from .base_page import BasePage



class BasketPage(BasePage):
    
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Корзина не пуста"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Текста 'Корзина пуста' нет"

    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Корзина пуста"

    def should_not_be_message_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "Присутствует текст 'Корзина пуста'"