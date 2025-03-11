from .locators import BasketPageLocators
from .base_page import BasePage



class BasketPage(BasePage):
    
    def should_not_be_items_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_message_basket_empty(self):
        self.is_element_present(*BasketPageLocators.BASKET_EMPTY)

    def should_be_items_in_basket(self):
        self.is_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_not_be_message_basket_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY)