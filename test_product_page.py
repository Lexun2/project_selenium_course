from .pages.product_page import ProductPage
import time, pytest

@pytest.mark.parametrize("promo",[
                                    "?promo=offer0",
                                    "?promo=offer1",
                                    "?promo=offer2",
                                    "?promo=offer3",
                                    "?promo=offer4",
                                    "?promo=offer5",
                                    "?promo=offer6",
                                    pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                    "?promo=offer8",
                                    "?promo=offer9",                                    
                                    ])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_page()