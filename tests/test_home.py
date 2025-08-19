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
    
def test_menu_books_click(home_page):
    home_page.books.click()
    assert "books" in home_page.page.url.lower(),f"the link is not:{home_page.page.url}"

    
@pytest.mark.parametrize("menu_method, expected_path", [
    ("bookmenuclick", "books"),
    ("computermenuclick", "computers"),
    ("electronicsmenuclick", "electronics"),
    ("apparelshoesmenuclick", "apparel-shoes"),
    ("degitalmenuclick", "digital-downloads"),
    ("jewelrymenuclick", "jewelry"),
    ("giftcardmenuclick", "gift-cards"),
])
def test_side_menu_clicks(home_page, menu_method, expected_path):
    click_method = getattr(home_page, menu_method)
    click_method()
    assert expected_path in home_page.page.url.lower(), f"{menu_method} failed: {home_page.page.url}"    

@pytest.mark.smoke   
def test_home_icon_click(home_page):
    home_page.logoclick()
    assert "https://demowebshop.tricentis.com/"   in home_page.page.url, f"Navigation is failed :{home_page.page.url}"

@pytest.mark.smoke    
def test_register_click(home_page):
    home_page.registerclick()
    assert "register" in home_page.page.url.lower(), f"Navigation is failed :{home_page.page.url.lower()}"  
    
@pytest.mark.smoke    
def test_login_click(home_page):
    home_page.loginclick()
    assert "login" in home_page.page.url.lower(), f"Navigation is failed :{home_page.page.url.lower()}"     

@pytest.mark.smoke    
def test_shopingcart_click(home_page):
    home_page.shopingcartclcik()
    assert "cart"   in home_page.page.url.lower(), f"Navigation is failed :{home_page.page.url.lower()}" 

@pytest.mark.smoke    
def test_wishlist_click(home_page):
    home_page.wishlistclick()
    assert "wishlist" in  home_page.page.url.lower(), f"Navigation is failed :{home_page.page.url.lower()}" 

@pytest.mark.smoke 
def test_Search_the_items(home_page):
    home_page.searchthequery("Science")
    assert "science" in home_page.page.url.lower(), f"Navigation is failed :{home_page.page.url.lower()}"

    