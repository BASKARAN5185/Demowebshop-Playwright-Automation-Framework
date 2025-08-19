from playwright.sync_api import Page
from pages.base_page import Baseclass

class Cartpage(Baseclass):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Top navigation/cart elements
        self.cartlink = page.locator("(//span[@class='cart-label'])[1]")
        self.addtocartbutton = page.locator("(//input[@value='Add to cart'])[1]")
        self.search_box = page.locator("#small-searchterms")
        self.search_button = page.locator("input.search-box-button")
        self.science_link = self.page.locator("a[href='/science']:text('Science')")


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

    # ---------------- Top Navigation / Cart Methods ----------------
    def clickCartLink(self):
        self.cartlink.click()

    def clickAddToCart(self):
        self.addtocartbutton.click()

    def searchthequery(self, query):
        # Perform search with the search box
        self.search_box.fill(query)
        self.search_box.press("Enter")

    # ---------------- Cart Page Info ----------------
    def getCartPageTitle(self):
        return self.cart_page_title.text_content()
    
    def clickScienceLink(self):
        # This will click the link with href='/science'
        self.science_link.click()

    def clickRemoveCheckbox(self):
        self.remove_checkbox.click()

    def isProductImageVisible(self):
        return self.product_image.is_visible()

    def getProductNameText(self):
        return self.product_name_link.text_content()

    def getUnitPrice(self):
        return self.unit_price.text_content()

    def getQuantityValue(self):
        return self.quantity_input.input_value()

    def getProductTotal(self):
        return self.product_total.text_content()

    # ---------------- Cart Buttons ----------------
    def clickUpdateCart(self):
        self.update_cart_button.click()

    def clickContinueShopping(self):
        self.continue_shopping_button.click()

    # ---------------- Coupons and Gift Cards ----------------
    def enterDiscountCode(self, code: str):
        self.discount_code_input.fill(code)

    def clickApplyDiscount(self):
        self.apply_discount_button.click()

    def enterGiftCardCode(self, code: str):
        self.gift_card_input.fill(code)

    def clickApplyGiftCard(self):
        self.apply_gift_card_button.click()

    # ---------------- Estimate Shipping ----------------
    def selectCountry(self, country: str):
        self.country_select.select_option(label=country)

    def selectState(self, state: str):
        self.state_select.select_option(label=state)

    def enterZipCode(self, zip_code: str):
        self.zip_input.fill(zip_code)

    def clickEstimateShipping(self):
        self.estimate_shipping_button.click()

    # ---------------- Totals ----------------
    def getSubtotalPrice(self):
        return self.subtotal_price.text_content()

    def getShippingPrice(self):
        return self.shipping_price.text_content()

    def getTaxPrice(self):
        return self.tax_price.text_content()

    def getOrderTotal(self):
        return self.order_total.text_content()

    # ---------------- Checkout ----------------
    def checkTermsAndConditions(self):
        self.terms_checkbox.check()

    def clickCheckout(self):
        self.checkout_button.click()
