from .pages.product_page import ProductPage
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




def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    """Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), "Не появилось сообщение о добавлении в корзину, хотя должно"




def test_guest_cant_see_success_message(browser): 
    """Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), "Появилось сообщение о добавлении в корзину, хотя не должно"

 


def test_message_disappeared_after_adding_product_to_basket(browser): 
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.is_disappeared(*ProductPageLocators.NAME_ITEM_IN_MESSAGE), "Не исчезает сообщение о добавлении в корзину"
