from playwright.sync_api import Page, expect

class Baseclass:
    
    def __init__(self,page : Page) :
        self.page=page
         
    def navigate(self,url :str) :
        self.page.goto(url, timeout=60000)
        
    def getPageTitle(self):
        return self.page.title()
    
    def geturl(self):
        return self.page.url
    
    def click(self,locator:str):
        self.page.click(locator)
        
    def waitforelement(self,locator:str,timeout:int =50000):   
        self.page.wait_for_selector(locator,timeout=timeout)
        
    def elementisvisible(self,locator:str) :
        try:
            return self.page.locator(locator).is_visible()
        except Exception :
            return False
        
    def fillthefield(self,locator:str,input:str):
        self.page.locator(locator).fill(input)    