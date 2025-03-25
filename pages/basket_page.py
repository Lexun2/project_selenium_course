from .locators import BasketPageLocators
from .base_page import BasePage
import time, requests
import os
from os import path

class BasketPage(BasePage):
    
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Element 'BASKET_ITEMS' is visible!"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Element 'BASKET_EMPTY' is not visible!"

    def should_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Element 'BASKET_ITEMS' is not visible!"
        file = f"basket_screenshot{time.time()}.png"
        os.makedirs('./tests/reports/screenshots', exist_ok = True)
        self.browser.find_element(*BasketPageLocators.BASKET_ITEMS).screenshot(f"./tests/reports/screenshots/{file}")
       
    def should_not_be_message_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "Element 'BASKET_EMPTY' is visible!"