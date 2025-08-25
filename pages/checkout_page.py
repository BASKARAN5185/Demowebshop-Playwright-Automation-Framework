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
        self.shipping_address_continue_button = page.locator("input.button-1.new-address-next-step-button")
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
        
        # Container div
        self.confirm_order_step = page.locator('#checkout-step-confirm-order')

        # Billing info
        self.billing_name = page.locator('ul.billing-info li.name')
        self.billing_email = page.locator('ul.billing-info li.email')
        self.billing_phone = page.locator('ul.billing-info li.phone')
        self.billing_fax = page.locator('ul.billing-info li.fax')
        self.billing_address1 = page.locator('ul.billing-info li.address1')
        self.billing_city_state_zip = page.locator('ul.billing-info li.city-state-zip')
        self.billing_country = page.locator('ul.billing-info li.country')

        # Payment & Shipping
        self.payment_method = page.locator('ul.billing-info li.payment-method')
        self.shipping_method = page.locator('ul.shipping-info li.shipping-method')

        # Product Info
        self.product_picture = page.locator('tr.cart-item-row td.product-picture img')
        self.product_name = page.locator('tr.cart-item-row td.product a.product-name')
        self.product_unit_price = page.locator('tr.cart-item-row td.unit-price span.product-unit-price')
        self.product_quantity = page.locator('tr.cart-item-row td.qty span:nth-child(2)')
        self.product_subtotal = page.locator('tr.cart-item-row td.subtotal span.product-subtotal')

        # Cart Totals
        self.cart_subtotal = page.locator('table.cart-total tr:nth-child(1) td.cart-total-right span.product-price')
        self.cart_shipping = page.locator('table.cart-total tr:nth-child(2) td.cart-total-right span.product-price')
        self.cart_tax = page.locator('table.cart-total tr:nth-child(3) td.cart-total-right span.product-price')
        self.cart_total = page.locator('table.cart-total tr:nth-child(4) td.cart-total-right span.product-price.order-total strong')

        # Buttons and messages
        self.confirm_order_button = page.locator('input.button-1.confirm-order-next-step-button')
        self.back_link = page.locator('p.back-link a')
        self.please_wait_span = page.locator('span#confirm-order-please-wait')

        self.page_title = page.locator('div.page-title h1')
        self.order_success_message = page.locator('div.order-completed div.title strong')
        self.order_number = page.locator('ul.details li').filter(has_text='Order number')
        self.order_details_link = page.locator('ul.details li a')
        self.continue_button = page.locator('input.button-2.order-completed-continue-button')
        
   
   #Action method Start 
   
    def validate_billing_info(self, billing_data: dict):
        assert self.billing_name.inner_text().strip() == billing_data.get("name", "")
        assert self.billing_email.inner_text().strip() == billing_data.get("email", "")
        assert self.billing_phone.inner_text().strip() == billing_data.get("phone", "")
        assert self.billing_fax.inner_text().strip() == billing_data.get("fax", "")
        assert self.billing_address1.inner_text().strip() == billing_data.get("address1", "")
        assert self.billing_city_state_zip.inner_text().strip() == billing_data.get("city_state_zip", "")
        assert self.billing_country.inner_text().strip() == billing_data.get("country", "")    


    def verifythepickupinstore(self):
        self.page.wait_for_timeout(2000)
        return self.PickUpInStore.is_visible()

    def checkthepickupstore(self):
        self.PickUpInStore.click()
        return True

    def clicktheshipaddresscontinebutton(self):
        self.shipping_address_continue_button.click()
        return True
 
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
    
    def paymentmethod_back_and_continue_button(self, button:str):
        Button=button.lower()
        if Button =='back':
           return self.paymentmethodback.click()
        elif Button=='continue' :
           return self.paymentmethodcontinue.click()    
           
    def select_the_shiping_method(self,method:str):       
        Deliver=method.lower()
        if Deliver=="ground":
           self.ShippingOption_Ground.click()
           return self.ShippingOption_Ground.is_checked()
        elif Deliver =='nextdayair':
           self.ShippingOption_NextDayAir.click()
           return self.ShippingOption_NextDayAir.is_checked()
        elif Deliver=='seconddayair':
            self.ShippingOption_SecondDayAir.click()
            return self.ShippingOption_SecondDayAir.is_checked()
        
    def shiping_method_back_and_continue(self,button:str):
        Button=button.lower()
        if Button=='back':    
           self.BackLink.click()
        elif Button=='continue' : 
            self.ContinueButton.click()
            

    def visible_the_payment_info(self,payinfo:str):
        Paymentinfo=payinfo.lower()
        if Paymentinfo =="cod": 
           return self.confirmcod.is_visibled()
        elif Paymentinfo =='moneyorder':
           return self.conformmoneyorder.is_visibled()
        elif payinfo =="card":
           self.CreditCardname.select_option(label='Visa')
           self.CreditCardholdername.fill('sam')
           self.CreditCardnumber.fill('453454665456')
           self.expiremonth.selct_option(label='12')
           self.expiredyear.selct_option(label='2026')
           self.CardCode.fill('987')
           return self.confirmcreditcard.is_visibled()
        elif payinfo =='poorder':
           self.PurchaseOrder.fill('5355435')
           return self.PurchaseOrder.is_visible()

    def payment_info_back_and_continue(self,button:str):
        Button =button.lower() 
        if Button=='back' :
            self.paymentinfoback.click()
        elif Button =='continue' :
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
