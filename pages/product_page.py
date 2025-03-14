from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def add_to_basket(self):
        ProductPageLocators.BUTTON_ADD_TO_BASKET
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
    
    def should_be_product_page(self):
        self.should_be_product_name_in_message()
        self.should_be_offer_in_message()
        self.should_be_price_in_message()

    def should_be_product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_ITEM).text == self.browser.find_element(*ProductPageLocators.NAME_ITEM_IN_MESSAGE).text, "Неверное имя товара в сообщении"

    def should_be_offer_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.OFFER).text == "Deferred benefit offer", "Не найден элемент с условиями предложения (Deferred benefit offer)"

    def should_not_be_offer_in_message(self):
        assert not self.browser.find_element(*ProductPageLocators.OFFER).text == "Deferred benefit offer", "Найден элемент с условиями предложения (Deferred benefit offer)"

    def should_be_price_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text == self.browser.find_element(*ProductPageLocators.SUMM_BASKET).text, "Суммы не сходятся, либо элементы не найдены"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), ("Success message(NAME_ITEM_IN_MESSAGE) is presented, but should not be")
        assert self.is_not_element_present(*ProductPageLocators.OFFER), ("Success message(OFFER) is presented, but should not be")

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), ("Success message is presented(NAME_ITEM_IN_MESSAGE), but should disappeared")
        assert self.is_disappeared(*ProductPageLocators.OFFER), ("Success message(OFFER) is presented, but should disappeared")