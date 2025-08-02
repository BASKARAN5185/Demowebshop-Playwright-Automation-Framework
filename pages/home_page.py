from playwright.sync_api import Page
from pages.base_page import Baseclass

class HomePage(Baseclass):
    def __init__(self,page):
        super().__init__(page)
        #Haeaers
        self.home_page_icon=page.locator("img[alt='Tricentis Demo Web Shop']")
        self.register=page.locator("text='Register'")
        self.login=page.locator(".ico-login")
        self.shopping_cart=page.locator("text='Shopping cart'")
        self.wishlist=page.locator("text='Wishlist'")
        self.search_box=page.locator('[name="q"]')
        self.newsletter_button=page.locator("#newsletter-subscribe-button")
        self.search_button=page.locator("#button-1 search-box-button")
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

    def logoclick(self):
        self.home_page_icon.click()
        
    def registerclick(self):
        self.register.click()
        
    def loginclick(self):
        self.login.click()
    
    def shopingcartclcik(self):
        self.shopping_cart.click()
        
    def wishlistclick(self):
        self.wishlist.click()
        
    def searchthequery(self,query ):
        self.search_box.fill(query)
        self.search_button.click()                        
       
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

    def bookmenuclick(self):  
        self.books.hover()
        self.books.click()
        
    def computermenuclick(self):
        self.computers.hover()
        self.computers.click()
    
    def electronicsmenuclick(self):
        self.electronics.hover()
        self.electronics.click()
    
    def apparelshoesmenuclick(self):
        self.apparel_shoes.hover()
        self.apparel_shoes.click()
        
    def degitalmenuclick(self):
        self.digital_downloads.hover()
        self.digital_downloads.click()
        
    def jewelrymenuclick(self):
        self.jewelry.hover()
        self.jewelry.click()
        
    def giftcardmenuclick(self):
        self.gift_cards.hover()
        self.gift_cards.click()
    
        
    
    
