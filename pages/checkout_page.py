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
        self.PickUpInStore = self.page.locator("//input[@id='PickUpInStore']")
        self.shipping_address_continue_button = self.page.locator("#shipping-buttons-container input.button-1.new-address-next-step-button")
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
        self.confirmcod=page.locator("#checkout-payment-info-load")
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
        self.paymentinfocontinue = self.page.locator("input.payment-info-next-step-button")
        
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
        self.confirm_order_Continue_button = page.locator('input.button-1.confirm-order-next-step-button')
        self.Confirm_order_back_button = page.locator('p.back-link a')
        self.please_wait_span = page.locator('span#confirm-order-please-wait')

        self.Completed_page_title = page.locator('div.page-title h1')
        self.Completed_order_success_message = page.locator('div.order-completed div.title strong')
        self.Completed_order_number = page.locator('ul.details li').filter(has_text='Order number')
        self.Completed_order_details_link = page.locator('ul.details li a')
        self.Completed_continue_button = page.locator('input.button-2.order-completed-continue-button')
        
   
   #Action method Start 

    def validate_billing_info(self, billing_data: dict):
         actual_data = {
          "name": self.billing_name.inner_text().strip(),
          "email": self.billing_email.inner_text().replace("Email:", "").strip(),
          "phone": self.billing_phone.inner_text().replace("Phone:", "").strip(),
          "fax": self.billing_fax.inner_text().replace("Fax:", "").strip(),
          "address1": self.billing_address1.inner_text().strip(),
          #"city_state_zip": self.billing_city_state_zip.inner_text().strip(),
          "country": self.billing_country.inner_text().strip(),
          }

         for key, expected in billing_data.items():  # ✅ Must be inside the method!
            actual = actual_data[key]
            print(f"\n🔍 Checking '{key}':")
            print(f"   Expected: '{expected}'")
            print(f"   Actual  : '{actual}'")
            assert actual == expected, f"❌ Mismatch in '{key}': expected '{expected}', got '{actual}'"


    def validate_payment_and_shiping(self, shipping_data: dict):
    # Collect actual values
         shipping_data_actual = {
            'Payment Method': self.payment_method.inner_text().strip(),
          'Shipping Method': self.shipping_method.inner_text().strip()
         }

    # Compare actual vs expected
         for key, expected in shipping_data.items():
              actual = shipping_data_actual.get(key)
              print(f"\n🔍 Checking '{key}':")
              print(f"   Expected: '{expected}'")
              print(f"   Actual  : '{actual}'")
         assert actual == expected, f"❌ Mismatch in '{key}': expected '{expected}', got '{actual}'"
         
    
    def validate_product_info(self, product_info_data: dict):
             actual_product_data_info={
              'Product Name' : self.product_name.inner_text().strip(),
              'Unit Price' : self.product_unit_price.inner_text().strip(),
              'Quantity'   : self.product_quantity.inner_text().strip() ,
              'Product subtotal' : self.product_subtotal.inner_text().strip()
             }   
         
             for key,expected in product_info_data.items():
                  actual=actual_product_data_info.get(key)  
                  print (f"\n checking : {key}")
                  print (f"expected : {expected}")
                  print (f"actual : {actual}")
                  assert actual==expected , f" key Value is :{key} ,expected value is :{expected},but get the value:{actual}"
                  
    def validate_cart_product(self, cart_product : dict):
             cart_product_data = {
               'Cart Subtotal' : self.cart_subtotal.inner_text().strip(),
               'Cart Shipping' : self.cart_shipping.inner_text().strip(),
               'Cart Tax' : self.cart_tax.inner_text().strip(),
              # 'Cart Total' : self.cart_total.inner_text().strip()
             }
             
             for key ,expected_value in cart_product.items():
                 getdata=cart_product_data.get(key)
                 print(f"/n kay value :{key}")
                 print(f"expect :{expected_value}")
                 print(f"actual : {getdata}")
                 assert getdata == expected_value , f"{key}:{key} -Expected :{expected_value} -get value :{getdata}"   
                 
    def confirm_order_back_and_continue(self, button1: str):
       button2 = button1.lower()
       try:
         if button2 == 'back':
             self.Confirm_order_back_button.click()
             return True
         elif button2 == 'continue':
             self.confirm_order_Continue_button.click()
             return True
         else:
             print('[ERROR] - Invalid button argument provided to confirm_order_back_and_continue')
             return False
       except Exception as e:
              print(f'[ERROR] Exception during confirm_order_back_and_continue: {e}')
              return False
 
             
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
        try:
            if Button =='back':
               self.paymentmethodback.click()
            elif Button=='continue' :
               self.paymentmethodcontinue.click()    
            else:
                print(f"[ERROR] Argument in the button clcik :{button}")
                return False
            return True     
        except Exception as e :
              print(f"[ERROR] exception in the button :{e}")
              return False
      

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
        try:
            if Paymentinfo =="cod": 
               self.confirmcod.wait_for(state ='visible' , timeout=5000)
               return True
        
            elif Paymentinfo =='moneyorder':
               return self.conformmoneyorder.is_visible(timeout=3000)
        
            elif payinfo =="card":
              self.CreditCardname.select_option(label='Visa')
              self.CreditCardholdername.fill('sam')
              self.CreditCardnumber.fill('453454665456')
              self.expiremonth.select_option(label='12')
              self.expiredyear.select_option(label='2026')
              self.CardCode.fill('987')
              return self.confirmcreditcard.is_visible(timeout=3000)
        
            elif payinfo =='poorder':
              self.PurchaseOrder.fill('5355435')
              return self.PurchaseOrder.is_visible(timeout=3000)
            
            else :
                print(f"[ERROR] Message of paymment method:{payinfo}")
                return False

        except Exception as e:
                print(f"[ERROR] of the paymentinfo :{e}") 
                return False       

    def payment_info_back_and_continue(self, button: str):
         button = button.lower()
         if button == 'back':
            self.paymentinfoback.click()
         elif button == 'continue':
            self.paymentinfocontinue.wait_for(state="visible", timeout=10000)
            self.paymentinfocontinue.click()
            return True
         else:
            print(f"[ERROR] Invalid button: {button}")
                

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
   
    def Validate_completed_page_data(self,complete_page= dict):
         completed_page_content = {
            'page_title' : self.Completed_page_title.inner_text().strip(),
            'success_message' : self.Completed_order_success_message.inner_text().strip() ,
            # 'order_number' : self.Completed_order_number.inner_text().strip() 
          }
         
         for key,expected in complete_page.items() :
             actual= completed_page_content.get(key)
             print(f"/n key :{key}")
             print(f"expected : {expected}")
             print(f"Actual : {actual}")
             assert actual==expected , f'key-{key} , expected value - {expected},actual value -{actual}'    
         
       
    def complete_order_details_link(self):   
         self.Completed_order_details_link.click()
         url= self.geturl
         return url
        
    def complete_order_continue_click(self):    
        self.Completed_continue_button.click()
        return True