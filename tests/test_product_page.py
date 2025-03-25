from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest, time, allure
from faker import Faker




class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse = True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        faker = Faker('ru_RU')
        login_page.register_new_user(faker.email(), 'bke75!ederrf45')
        login_page.should_be_authorized_user()


    @allure.feature('Product')
    @allure.story('Product Feature')
    @allure.title("Тест заанее проваленный у авторизованного пользователя")
    @pytest.mark.xfail(reason="Now not work!")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser): 
        """Открываем страницу товара 
        Добавляем товар в корзину 
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_not_be_success_message()
       
    @allure.feature('Product')
    @allure.story('Product Feature')
    @allure.title("Тест добавления товара в корзины авторизованным пользователем")
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_product_page()


@allure.feature('Basket')
@allure.story('Basket Feature')
@allure.title("Тест заранее проваленный")
@pytest.mark.xfail(reason="Now not work!")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    """Открываем страницу товара 
    Добавляем товар в корзину 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    time.sleep(5)
    product_page.should_not_be_success_message()


@allure.feature('Product')
@allure.story('Product Feature')
@allure.title("Тест появления сообщений при добавлении товара в корзину")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.need_review
@pytest.mark.parametrize("promo",[
                                    0 \
                                    # , 1, 2, 3, 4, 5, 6,
                                    # pytest.param(7, marks=pytest.mark.xfail),
                                    # 8, 9                                   
                                    ])
# @pytest.mark.parametrize("promo",[ num if num!=7 else pytest.param(num, marks=pytest.mark.xfail) for num in range(10) ])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_page()


@allure.feature('Product')
@allure.story('Product Feature')
@allure.title("Тест отсутствия сообщений о добавлении в корзину при открытии страницы продукта")
@allure.severity(allure.severity_level.NORMAL)
def test_guest_cant_see_success_message(browser): 
    """Открываем страницу товара 
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

 
@allure.feature('Basket')
@allure.story('Basket Feature')
@allure.title("Тест заранее проваленный")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail(reason="This feature in progress! Now not work!")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()
    browser.save_screenshot('screenie.png')
    #     # Параметры type="jpeg"|"png", full_page=True|False, quality = Качество сжатия изображения для формата 'jpeg'(0-100), 
    #     # clip (dict): Задает область для создания скриншота, указав координаты x, y, ширину и высоту.
    #     # omit_background (bool): Позволяет убрать фон изображения. Если True, фон на скриншоте будет прозрачным, что актуально в случае формата 'png'. По умолчанию значение False.
    #     # timeout (float | int): Задает максимальное время ожидания (в миллисекундах) перед созданием скриншота. По умолчанию 30000 миллисекунд (30 секунд).
    #     # скриншот страницы
    #     page.screenshot(path="screenshot1.png")
    #     # скриншот всей страницы (скриншот всей страницы (True) или только видимой области (False-дефолт))
    #     page.screenshot(path="screenshot2.png", full_page=False, type="jpeg", quality=50, clip={"x": 50, "y": 0, "width": 400, "height": 300}, omit_background=False, timeout=10000)
    #     # скриншот элемента
    #     page.locator("#dzen-header > div.dzen-layout--desktop-base-header__logoContainer-pu.dzen-layout--desktop-base-header__isMorda-2n > a > svg.dzen-layout--desktop-base-header__logo-2H.dzen-layout--desktop-base-header__isMorda-2n").screenshot(path="screenshot3.png")
  


@allure.feature('Login')
@allure.story('Login Feature')
@allure.title("Тест видимости кнопки 'Войти' со страницы любого товара")
@allure.severity(allure.severity_level.CRITICAL)
def test_guest_should_see_login_link_on_product_page(browser):
    """Гость видит Кнопку Войти со страницы любого товара"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@allure.feature('Login')
@allure.story('Login Feature')
@allure.title("Тест работоспособности кнопки 'Войти' со страницы любого товара")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Гость может нажать кнопку Войти со страницы любого товара"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@allure.feature('Basket')
@allure.story('Basket Feature')
@allure.title("Тест надписей пустой корзины и не пустой")
@allure.description("Сначала мы заходим переходим со страницы продукта в корзиу, проверем что она пустая, потом возвращаемся к продукту, кладём его в корзину," /
                    " переходим в корзину и проверяем что корзина не пустая и в нем есть элемент товара.")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    with allure.step('Открываем страницу товара'):
        product_page = ProductPage(browser, link)
        product_page.open()
    with allure.step('Переходим на страницу корзины'):
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
    with allure.step('Проверяем отсутствие товаров в корзине и присутствие надписи "Корзина пуста"'):
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_message_basket_empty()
    with allure.step('Переходим на страницу товара'):
        product_page.open()
        product_page = ProductPage(browser, link)  
    with allure.step('Добавляем товар в корзину'):
        product_page.add_to_basket()
    time.sleep(1)
    with allure.step('Переходим в корзину и проверяем что она не пуста'):
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_items_in_basket()
        basket_page.should_not_be_message_basket_empty()
