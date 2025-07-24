from pages.base_page import Baseclass

class Loginpage(Baseclass):

    def __init__(self, page):
        super().__init__(page)
        self.username = "#Email"
        self.password = "#Password"
        self.loginbutton = "[class='button-1 login-button']"
        self.forgetpasslink = ""  

    def enterusername(self, email: str):
        self.fillthefield(self.username, email)

    def enterthepass(self, password: str):
        self.fillthefield(self.password, password)

    def clicktheloginbutton(self):
        self.click(self.loginbutton)

    def login(self, user1: str, passw1: str):
        self.enterusername(user1)
        self.enterthepass(passw1)
        self.clicktheloginbutton()
