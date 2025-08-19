from pages.cart_page import Cartpage
import pytest

@pytest.fixture
def cartpage(page):   # 'page' is Playwright's built-in fixture
    Cart = Cartpage(page)
    Cart.navigate("https://demowebshop.tricentis.com/cart")
    return Cart

def test_clickthecartlink(cartpage):
    cartpage.clickCartLink()
    assert "cart" in cartpage.geturl()  # note parentheses here for method call
