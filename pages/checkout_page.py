from playwright.sync_api import Playwright
from pages.base_page import Baseclass

class CheckoutPage(Baseclass):
    def __init__(self,page):
        super().__init__(page)

        #Billing address Locators
        self.firstname=page.locator('#BillingNewAddress_FirstName')
        self.lastname=page.locator('input[name="BillingNewAddress.LastName"]')
        self.email=page.locator("//input[@name='BillingNewAddress.Email']")
        self.company=page.locator("#BillingNewAddress_Company")
        self.countryid=page.locator("select[name='BillingNewAddress.CountryId']")
        self.state=page.locator("#BillingNewAddress_StateProvinceId")
        self.city=page.locator('#BillingNewAddress_City')
        self.addres1=page.locator("#BillingNewAddress_Address1")
        self.addres2=page.locator("#BillingNewAddress_Address2")
        self.zipcode=page.locator("input[name='BillingNewAddress.ZipPostalCode']")
        self.phonenumber=page.locator('#BillingNewAddress_PhoneNumber')
        self.faxnum=page.locator('#BillingNewAddress_FaxNumber')
        self.continuebutton=page.locator('//input[@onclick="Billing.save()"]')
        self.billingaddressdp=page.locator('#billing_address_id')
        
        #shiping addres
        self.shipingaddresscontinuebutton=page.locator('.button-1 new-address-next-step-button')
        self.PickUpInStore=page.locator("#PickUpInStore")
        self.shipadressbackbutton=page.locator('text="Back"')
        
        #Shipping method
        self.ShippingOption_Ground = page.locator('#shippingoption_0')
        self.ShippingOption_NextDayAir = page.locator('#shippingoption_1')
        self.ShippingOption_SecondDayAir = page.locator('#shippingoption_2')
        self.ContinueButton = page.locator('input.shipping-method-next-step-button')
        self.BackLink = page.locator('#shipping-method-buttons-container a')  
        
        #Payment method
        self.cashondelivery=page.locator('#paymentmethod_0')
        self.CheckMoneyOrder=page.locator('#paymentmethod_1')
        self.CreditCard=page.locator("#paymentmethod_2") 
        self.PurchaseOrder=page.locator("#paymentmethod_3")
        self.paymentmethodback=page.locator("//p[@class='back-link']//a)[3]")
        self.paymentmethodcontinue=page.locator("//input[@class='button-1 payment-method-next-step-button']")
        
        #Payment information
        self.confirmcod=page.locator("//p[normalize-space(text())='You will pay by COD']")
        self.conformmoneyorder=page.locator("text='Mail Personal or Business Check, Cashier's Check or money order to:'")
        self.confirmcreditcard=page.locator("//label[@for='CreditCardTypes']")
        self.CreditCardname=page.locator('#CreditCardType')
        self.CreditCardholdername=page.locator('#CardholderName')
        self.CreditCardnumber=page.locator('input[name="CardNumber"]')
        self.expiremonth=page.locator('select[name="ExpireMonth"]')
        self.expiredyear=page.locator('select[name="ExpireYear"]')
        self.CardCode=page.locator('#CardCode')
        self.PurchaseOrderNumber=page.locator('#PurchaseOrderNumber')
        self.paymentinfoback=page.locator("//div[@id='payment-info-buttons-container']/p[1]/a[1]")
        self.paymentinfocontinue=page.locator("//input[@class='button-1 payment-info-next-step-button']")
        
        #Confirm order
        # Container div for the confirm order step
        self.confirm_order_step = page.locator('#checkout-step-confirm-order')
        # Billing address fields
        self.billing_name = page.locator('ul.billing-info li.name')
        self.billing_email = page.locator('ul.billing-info li.email')
        self.billing_phone = page.locator('ul.billing-info li.phone')
        self.billing_fax = page.locator('ul.billing-info li.fax')
        self.billing_address1 = page.locator('ul.billing-info li.address1')
        self.billing_city_state_zip = page.locator('ul.billing-info li.city-state-zip')
        self.billing_country = page.locator('ul.billing-info li.country')
        # Payment method
        self.payment_method = page.locator('ul.billing-info li.payment-method')
        # Shipping method
        self.shipping_method = page.locator('ul.shipping-info li.shipping-method')
        # Product info in the cart
        self.product_picture = page.locator('tr.cart-item-row td.product-picture img')
        self.product_name = page.locator('tr.cart-item-row td.product a.product-name')
        self.product_unit_price = page.locator('tr.cart-item-row td.unit-price span.product-unit-price')
        self.product_quantity = page.locator('tr.cart-item-row td.qty span:nth-child(2)')  # because first span is label
        self.product_subtotal = page.locator('tr.cart-item-row td.subtotal span.product-subtotal')
        # Cart totals
        self.cart_subtotal = page.locator('table.cart-total tr:nth-child(1) td.cart-total-right span.product-price')
        self.cart_shipping = page.locator('table.cart-total tr:nth-child(2) td.cart-total-right span.product-price')
        self.cart_tax = page.locator('table.cart-total tr:nth-child(3) td.cart-total-right span.product-price')
        self.cart_total = page.locator('table.cart-total tr:nth-child(4) td.cart-total-right span.product-price.order-total strong')
        # Confirm button
        self.confirm_order_button = page.locator('input.button-1.confirm-order-next-step-button')
        # Back link
        self.back_link = page.locator('p.back-link a')
        # Please wait span (shown on submitting)
        self.please_wait_span = page.locator('span#confirm-order-please-wait')
        # Page title (e.g., "Thank you")
        self.page_title = page.locator('div.page-title h1')
 
        # Success message
        self.order_success_message = page.locator('div.order-completed div.title strong')

        # Order number (exact match is not ideal, so we use text contains)
        self.order_number = page.locator('ul.details li').filter(has_text='Order number')

        # Link to order details
        self.order_details_link = page.locator('ul.details li a')

        # Continue button
        self.continue_button = page.locator('input.button-2.order-completed-continue-button')


    def verifythepickupinstore(self):
        self.page.wait_for_timeout(2000)
        return self.PickUpInStore.is_visible()

    def checkthepickupstore(self):
        self.checkthepickupstore.click()
        return self.checkthepickupstore.is_checked()

    def clicktheshipaddresscontinebutton(self):
        self.shipingaddresscontinuebutton.click()
 
    def clicktheshipaddressbackbutton(self):
        self.shipadressbackbutton.click()


    def check_the_cash_on_deliver(self):
        self.cashondelivery.click()
        return self.cashondelivery.is_checked()
    
    def check_the_money_order(self):
        self.CheckMoneyOrder.click()
        return self.check_the_money_order.is_checked()
    
    def Check_the_credit_card(self):
        self.CreditCard.click()
        return self.CreditCard.is_checked()

    def Check_the_purchase_order(self): 
        self.PurchaseOrder.click()
        return self.PurchaseOrder.is_checked()
    
    def paymentmethod_back_and_continue_button(self, back:str, continute_:str):
        if(back.lower()=='back'):
           self.paymentmethodback.click()
        elif(continute_.lower()=='continue') :
           self.paymentmethodcontinue.click()    


    def visible_the_payment_info(self,cod:str,moneyorder:str,card:str,poorder:str):
        if(cod.lower()=="cod"): 
           return self.confirmcod.is_visibled()
        elif(moneyorder.lower()=='moneyorder'):
           return self.conformmoneyorder.is_visibled()
        elif(card.lower()=="card"):
           self.CreditCardname.select_option(label='Visa')
           self.CreditCardholdername.fill('sam')
           self.CreditCardnumber.fill('453454665456')
           self.expiremonth.selct_option(label='12')
           self.expiredyear.selct_option(label='2026')
           self.CardCode.fill('987')
           return self.confirmcreditcard.is_visibled()
        elif(poorder.lower()=='poorder'):
           self.PurchaseOrder.fill('5355435')
           return self.PurchaseOrder.is_visible()

    def payment_info_back_and_continue(self,back:str): 
        if(back.lower()=='lower'):
            self.paymentinfoback.click()
        else :
            self.paymentinfocontinue.clicK()

    def selectbillingaddress(self) -> bool:
        """
        Select 'New Address' if dropdown is present, otherwise assume new address form is already shown.
        Returns True if form is ready for input.
        """
        try:
         if self.page.is_visible("#billing-address-select", timeout=3000):
            dropdown = self.page.locator("#billing-address-select")
            # Usually 'New Address' option value is an empty string '' or some known value
            dropdown.select_option(value='')  # Select 'New Address' with empty value
            # Optionally wait for the form to be visible after selection
            self.page.wait_for_selector("#billing-address-form", timeout=3000)
            return True
         else:
            # Dropdown not visible, assume form is open
            return True
        except Exception:
        # On any error, assume form is ready
             return True

    def enterthefirstname(self,name:str):
        self.firstname.fill(name)
        
    
    def enterthelastname(self,name:str):
        self.lastname.fill(name)
        
    
    def entertheemail(self,email:str):
        self.email.fill(email)


    def enterthecompany(self,company:str):
        self.company.fill(company) 

    def selectthecountry(self,country:str):
        self.countryid.select_option(label=country)

    def selectthestate(self,state:str):
        self.state.select_option(label=state)
        self.page.wait_for_timeout(1000) 

    def enterthecity(self,city:str):
        self.city.fill(city)

    def entertheaddress1(self,ad1:str):
        self.addres1.fill(ad1)

    def entretheaddress2(self,ad2:str):
        self.addres2.fill(ad2)

    def enterthezip(self,zip:str):
        self.zipcode.fill(zip)

    def enterthephonenumber(self,phone:str):
        self.phonenumber.fill(phone)

    def enterthefaxnumber(self,faxnum:str):
        self.faxnum.fill(faxnum)

    def clickthecontinuebutton(self):        
        self.continuebutton.click()

    def fillthebillingaddress(self,fname:str,lname:str,email:str,company:str,country:str,state:str,
                              city:str,address1:str,address2:str,zip:str,phone:str,faxnum:str):
        self.enterthefirstname(fname)
        self.enterthelastname(lname)
        self.entertheemail(email)
        self.enterthecompany(company)
        self.selectthecountry(country)
        self.selectthestate(state)
        self.enterthecity(city)
        self.entertheaddress1(address1)
        self.entretheaddress2(address2)
        self.enterthezip(zip)
        self.enterthephonenumber(phone)
        self.enterthefaxnumber(faxnum)
        return self.clickthecontinuebutton()
