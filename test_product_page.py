from .pages.product_page import ProductPage
import time, pytest

# @pytest.mark.parametrize("promo",[
#                                     0, 1, 2, 3, 4, 5, 6,
#                                     pytest.param(7, marks=pytest.mark.xfail),
#                                     8, 9                                   
#                                     ])
@pytest.mark.parametrize("promo",[ num if num!=7 else pytest.param(num, marks=pytest.mark.xfail) for num in range(10) ])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_product_page()