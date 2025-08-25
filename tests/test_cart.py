import pytest
from pages.cart_page import Cartpage


@pytest.fixture(scope='class')
def cart_page(page):
    # Initialize Cartpage instance
    cartpage = Cartpage(page)
    # Navigate to the cart page and search/add product before each test
    cartpage.navigate("https://demowebshop.tricentis.com/cart")
    cartpage.searchthequery('Science')  # Search for product
    cartpage.clickScienceLink()
    cartpage.clickAddToCart()  # Add product to cart
    cartpage.clickCartLink()
    return cartpage


class TestCartPage:

    def test_click_cart_link(self, cart_page):
        # Test that clicking on the cart link redirects to the cart page
        cart_page.clickCartLink()
        assert "cart" in cart_page.page.url.lower()

    def test_get_cart_page_title(self, cart_page):
        # Test that the cart page has the correct title
        title = cart_page.getCartPageTitle()
        assert title and "Shopping cart" in title

    def test_click_add_to_cart(self, cart_page):
        # Test that adding to the cart works
        cart_page.searchthequery('Science')
        cart_page.clickAddToCart()
        assert "Shopping cart" in cart_page.page.url.lower()

    def test_click_remove_checkbox(self, cart_page):
        # Test that the remove checkbox works as expected
        cart_page.clickRemoveCheckbox()

    def test_product_image_visible(self, cart_page):
        # Check if the product image is visible on the cart page
        assert cart_page.isProductImageVisible()

    def test_get_product_name_text(self, cart_page):
        # Test to get product name and check it's not empty
        name = cart_page.getProductNameText()
        assert name and len(name) > 0

    def test_get_unit_price(self, cart_page):
        # Check that the unit price starts with "$"
        price = cart_page.getUnitPrice().strip()  # Clean up any unwanted whitespace
        assert price and price.startswith("$")

    def test_get_quantity_value(self, cart_page):
        # Check the quantity value in the cart
        quantity = cart_page.getQuantityValue()
        assert quantity.isdigit()

    def test_get_product_total(self, cart_page):
        # Check that the product total starts with "$"
        total = cart_page.getProductTotal().strip()  # Clean up any unwanted whitespace
        assert total and total.startswith("$")

    def test_click_update_cart(self, cart_page):
        # Test that the update cart button works
        cart_page.clickUpdateCart()

    def test_click_continue_shopping(self, cart_page):
        # Test that the continue shopping button works
        cart_page.clickContinueShopping()

    def test_apply_discount_code(self, cart_page):
        # Test applying a discount code
        cart_page.enterDiscountCode("DISCOUNT2025")
        cart_page.clickApplyDiscount()

    def test_apply_gift_card(self, cart_page):
        # Test applying a gift card code
        cart_page.enterGiftCardCode("GIFTCARD123")
        cart_page.clickApplyGiftCard()

    def test_estimate_shipping(self, cart_page):
        # Test estimating shipping with country, state, and zip
        cart_page.selectCountry("United States")
        cart_page.selectState("California")
        cart_page.enterZipCode("90001")
        cart_page.clickEstimateShipping()

    def test_get_totals(self, cart_page):
        # Get and check the totals (subtotal, shipping, tax, total)
        subtotal = cart_page.getSubtotalPrice().strip()  # Clean up any unwanted whitespace
        shipping = cart_page.getShippingPrice().strip()  # Clean up any unwanted whitespace
        tax = cart_page.getTaxPrice().strip()  # Clean up any unwanted whitespace
        order_total = cart_page.getOrderTotal().strip()  # Clean up any unwanted whitespace
        assert subtotal and shipping and tax and order_total

    def test_checkout_process(self, cart_page):
        # Check that the checkout process works (terms and conditions checkbox)
        cart_page.checkTermsAndConditions()
        cart_page.clickCheckout()
