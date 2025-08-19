from playwright.sync_api import Page
from base_page import Baseclass
import re

class Cartpage(Baseclass):
    def __init__(self, page: Page):
        super().__init__(page)

        # Top navigation/cart elements
        self.cartlink = page.locator("(//span[@class='cart-label'])[1]")
        self.addtocartbutton = page.locator("(//input[@value='Add to cart'])[1]")

        # Shopping cart page
        self.cart_page_title = page.locator("h1", has_text="Shopping cart")
        self.remove_checkbox = page.locator("(//input[@name='removefromcart'])[1]")
        self.product_image = page.locator("(//td[@class='product-picture']//img)[1]")
        self.product_name_link = page.locator("(//a[@class='product-name'])[1]")
        self.unit_price = page.locator("(//span[@class='product-unit-price'])[1]")
        self.quantity_input = page.locator("(//input[contains(@class, 'qty-input')])[1]")
        self.product_total = page.locator("(//span[@class='product-subtotal'])[1]")

        # Cart buttons
        self.update_cart_button = page.locator("input[name='updatecart']")
        self.continue_shopping_button = page.locator("input[name='continueshopping']")

        # Coupons and gift cards
        self.discount_code_input = page.locator("input[name='discountcouponcode']")
        self.apply_discount_button = page.locator("input[name='applydiscountcouponcode']")
        self.gift_card_input = page.locator("input[name='giftcardcouponcode']")
        self.apply_gift_card_button = page.locator("input[name='applygiftcardcouponcode']")

        # Estimate shipping section
        self.country_select = page.locator("select#CountryId")
        self.state_select = page.locator("select#StateProvinceId")
        self.zip_input = page.locator("input#ZipPostalCode")
        self.estimate_shipping_button = page.locator("input[name='estimateshipping']")

        # Totals
        self.subtotal_price = page.locator("//td[@class='cart-total-right']/span/span[@class='product-price'][1]")
        self.shipping_price = page.locator("//td[@class='cart-total-right']/span/span[@class='product-price'][2]")
        self.tax_price = page.locator("//tr[td/span[contains(text(),'Tax:')]]//span[@class='product-price']")
        self.order_total = page.locator("span.product-price.order-total")

        # Checkout section
        self.terms_checkbox = page.locator("input#termsofservice")
        self.checkout_button = page.locator("button#checkout")
        
    def cartlinkclick(self):
         self.cartlink.click()
         
        
