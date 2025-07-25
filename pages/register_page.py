from pages.base_page import Baseclass

class RegisterPage(Baseclass):
    
    def __init__(self,page):
        super().__init__(page)
        self.malecheckbox="#gender-male"
        self.femalecheckbox="#gender-female"
        self.firstname="[name='FirstName']"
        self.lastname="[name='LastName']"
        self.gmail="[name='Email']"
        self.password="[name='Password']"
        self.confirmpass="[name='ConfirmPassword']"
        self.registerbutton="#register-button"
        
        
    def selectthegender(self,gender:str):
        if gender.lower() == 'male' :
           self.click(self.malecheckbox)
        elif gender.lower()=='female' :
           self.click(self.femalecheckbox) 
           
    def fillfrstname(self ,fname:str):
        self.fillthefield(self.firstname,fname)
        
    def fillthelastname(self,lname:str):
        self.fillthefield(self.lastname,lname)
        
    def fillemail(self,mail:str):
        self.fillthefield(self.gmail,mail)
        
    def fillthepass(self,password:str): 
        self.fillthefield(self.password,password)  
    
    def filltheconformpass(self,conformpass:str):
        self.fillthefield(self.confirmpass,conformpass) 
        
    def clicktheregistrationbutton(self):
        self.click(self.registerbutton)           
        
    def filltheregistrationform(self,gender:str,fname:str,lname:str,gmail:str,password:str,cpass:str):
        self.selectthegender(gender)
        self.fillfrstname(fname)
        self.fillthelastname(lname)
        self.fillemail(gmail)
        self.fillthepass(password)
        self.filltheconformpass(cpass)
        return self.clicktheregistrationbutton()
        
             
                 