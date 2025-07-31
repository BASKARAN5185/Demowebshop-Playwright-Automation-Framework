from playwright.sync_api import Page
from pages.base_page import Baseclass

class HomePage(Baseclass):
    def __init__(self,page):
        super().__init__(page)
        #Header meanu
        self.head_books = page.locator("ul.top-menu >> a[href='/books']")
        self.head_computers = page.locator("ul.top-menu >> a[href='/computers']")
        self.head_electronics = page.locator("ul.top-menu >> a[href='/electronics']")
        self.head_apparel_shoes = page.locator("ul.top-menu >> a[href='/apparel-shoes']")
        self.head_digital_downloads = page.locator("ul.top-menu >> a[href='/digital-downloads']")
        self.head_jewelry = page.locator("ul.top-menu >> a[href='/jewelry']")
        self.head_gift_cards = page.locator("ul.top-menu >> a[href='/gift-cards']")

        # Submenu under "Computers"
        self.head_desktops = page.locator("ul.sublist >> a[href='/desktops']").first
        self.head_notebooks = page.locator("ul.sublist >> a[href='/notebooks']").first
        self.head_accessories = page.locator("ul.sublist >> a[href='/accessories']").first

        # Submenu under "Electronics"
        self.head_camera_photo = page.locator("ul.sublist >> a[href='/camera-photo']").first
        self.head_cell_phones = page.locator("ul.sublist >> a[href='/cell-phones']").first
        
        #Sidemenu locators 
        self.books = page.locator("a[href='/books']")
        self.computers = page.locator("a[href='/computers']")
        self.electronics = page.locator("a[href='/electronics']")
        self.apparel_shoes = page.locator("a[href='/apparel-shoes']")
        self.digital_downloads = page.locator("a[href='/digital-downloads']")
        self.jewelry = page.locator("a[href='/jewelry']")
        self.gift_cards = page.locator("a[href='/gift-cards']")

       
    def headerbookmenuclick(self):  
        self.head_books.hover()
        self.head_books.click()
        
    def headercomputermenuclick(self):
        self.head_computers.hover()
        self.head_computers.click()
    
    def headerelectronicsmenuclick(self):
        self.head_electronics.hover()
        self.head_electronics.click()
    
    def headerapparelshoesmenuclick(self):
        self.head_apparel_shoes.hover()
        self.head_apparel_shoes.click()
        
    def headerdegitalmenuclick(self):
        self.head_digital_downloads.hover()
        self.head_digital_downloads.click()
        
    def headerjewelrymenuclick(self):
        self.head_jewelry.hover()
        self.head_jewelry.click()
        
    def headergiftcardmenuclick(self):
        self.head_gift_cards.hover()
        self.head_gift_cards.click()
    
    def headersubdesktopmenuclick(self):
        self.head_computers.click()
        self.head_desktops.hover()
        self.head_desktops.click()         
     
    def headersubnotebooksmenuclick(self):
        self.head_computers.click()
        self.head_notebooks.hover()
        self.head_notebooks.click()               
            
    def headersubaccessoriesmenuclick(self):
        self.head_computers.click()
        self.head_accessories.hover()
        self.head_accessories.click()    
        
    def headersubdesktopmenuclick(self):
        self.head_electronics.click()
        self.head_cell_phones.hover()
        self.head_cell_phones.click()      
        
    def headersubmenuclick(self):
        self.head_electronics.click()
        self.head_camera_photo.hover()
        self.head_camera_photo.click()


        
    
    
