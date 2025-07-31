from pages.home_page import HomePage
import pytest

@pytest.fixture
def home_page(page):
    homepage = HomePage(page)
    homepage.navigate("https://demowebshop.tricentis.com")
    return homepage

def test_header_books_click(home_page):
    home_page.headerbookmenuclick()
    assert "books" in home_page.page.url.lower(), f"Navigation failed, current URL: {home_page.page.url}"
    

def test_header_computers_clcik(home_page):
    home_page.headercomputermenuclick()
    assert "computers" in home_page.page.url.lower(), f"Navigation failed, current URL: {home_page.page.url}"
    
def test_header_electronics_clcik(home_page):
    home_page.headerelectronicsmenuclick()
    assert "electronics" in home_page.page.url.lower(), f"Navigation falied, current URL: {home_page.page.url}"    
    
def test_header_apperalandshoes_clcik(home_page):
    home_page.headerapparelshoesmenuclick()
    assert "apparel-shoes" in home_page.page.url.lower(), f"Navigation failed, current Url: {home_page.page.url}" 

def test_header_Digitaldwonload_click(home_page):
    home_page.headerdegitalmenuclick()
    assert "digital-downloads" in home_page.page.url.lower(), f"Navigation falied ,current Url: {home_page.page.url}"       
    
def test_header_jewelry_click(home_page):
    home_page.headerjewelrymenuclick()
    assert "jewelry" in home_page.page.url.lower(), f"Navigatio failed, current url :{home_page.page.url}"
    
def test_header_giftcard_click(home_page):
    home_page.headergiftcardmenuclick()
    assert "gift-cards"  in home_page.page.url.lower(), f"Navigation failed, current url :{home_page.page.url}"  
    
def test_header_notebooks_click(home_page):
    home_page.headersubnotebooksmenuclick()
    assert "notebooks" in home_page.page.url.lower(), f"Navigation failed, current url: {home_page.page.url}"

def test_header_accessories_click(home_page):
    home_page.headersubaccessoriesmenuclick()
    assert "accessories" in home_page.page.url.lower(), f"Navigation failed, current url: {home_page.page.url}"

def test_header_cell_phones_click(home_page):
    home_page.headersubcellphonesmenuclick()
    assert "cell-phones" in home_page.page.url.lower(), f"Navigation failed, current url: {home_page.page.url}"

def test_header_camera_photo_click(home_page):
    home_page.headersubmenuclick()
    assert "camera-photo" in home_page.page.url.lower(), f"Navigation failed, current url: {home_page.page.url}"

def test_header_desktop_click(home_page):
    home_page.headersubdesktopmenuclick()
    assert "desktops" in home_page.page.url.lower(), f"Navigation failed, current url: {home_page.page.url}"
    
    
    