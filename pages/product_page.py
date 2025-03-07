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
        assert self.browser.find_element(*ProductPageLocators.OFFER).text == "Deferred benefit offer", "Указаны не те условия предложения (OFFER)_"

    def should_be_price_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_ITEM).text == self.browser.find_element(*ProductPageLocators.SUMM_BASKET).text, "Указана неверная сумма корзины"

    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), "Сообщение с названием товара успешно добавленого в корзину не исчезает за выделенный timeout"
        assert self.is_disappeared(*ProductPageLocators.OFFER), "Сообщение с условиями предложения не исчезает за выделенный timeout"
