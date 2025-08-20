from playwright.sync_api import Playwright
from pages.base_page import Baseclass

class CheckoutPage(Baseclass):
    def __init__(self,page):
        super().__init__(page)
        self=self.page

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
        self.PickUpInStore=page.locator("#PickUpInStore")


    def verifythepickupinstore(self):
        return self.PickUpInStore.is_visible()

    def enterthefirstname(self,name:str):
        self.firstname.fill(name)
        
    
    def enterthelastname(self,name:str):
        billlname=self.lastname.fill(name)
        
    
    def entertheemail(self,email:str):
        self.email.fill(email)


    def enterthecompany(self,company:str):
        self.company.fill(company) 

    def selectthecountry(self,country:str):
        self.countryid.select_option(label=country)

    def selectthestate(self,state:str):
        self.state.select_option(value=state)

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

    def fillthebillingaddress(self,fname:str,lname:str,email:str,country:str,state:str,
                              city:str,address1:str,address2:str,zip:str,phone:str,faxnum:str):
        self.enterthefirstname(fname)
        self.enterthelastname(lname)
        self.entertheemail(email)
        self.selectthecountry(country)
        self.selectthestate(state)
        self.enterthecity(city)
        self.entertheaddress1(address1)
        self.entretheaddress2(address2)
        self.enterthezip(zip)
        self.enterthephonenumber(phone)
        self.enterthefaxnumber(faxnum)
        return self.clickthecontinuebutton()
