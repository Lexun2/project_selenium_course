from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
import time, pytest

@pytest.mark.parametrize("promo",[
                                    # 0, 1, 2, 3, 4, 5, 6,
                                    # pytest.param(7, marks=pytest.mark.xfail),
                                    # 8, 
                                    9                                   
                                    ])
# @pytest.mark.parametrize("promo",[ num if num!=7 else pytest.param(num, marks=pytest.mark.xfail) for num in range(10) ])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_page()
    product_page.should_not_be_success_message()



@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    """Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), "Не появилось сообщение о добавлении в корзину, хотя должно"



@pytest.mark.skip
def test_guest_cant_see_success_message(browser): 
    """Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), "Появилось сообщение о добавлении в корзину, хотя не должно"

 

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser): 
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.is_disappeared(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), "Не исчезает сообщение о добавлении в корзину"


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    """Гость видит Кнопку Войти со страницы любого товара"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Гость может нажать кнопку Войти со страницы любого товара"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_basket_empty()
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.go_to_basket_page()
    basket_page.should_be_items_in_basket()
    basket_page.should_not_be_message_basket_empty()
