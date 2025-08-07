from pages.login_page import Loginpage
import pytest

@pytest.mark.regression
def test_user_Login(login_page):
    login_page.login("anya", "Anya@123")
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" not in url, f"Login failed, still on login page: {url}"

@pytest.mark.regression
def test_Invalidusername(login_page):
    login_page.login("anya123","Anya@123")
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" in url, f"Expected to remain on login page but on: {url}"

@pytest.mark.regression    
def test_Invalidpassword(login_page):
    login_page.login("anya","sdasd")
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" in url, f"Expected to remain on login page but on: {url}"

@pytest.mark.regression    
def test_Invalidusernamepassword(login_page):
    login_page.login("anya1223","sdasd")
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" in url, f"Expected to remain on login page but on: {url}"

@pytest.mark.regression    
def test_emptyusername(login_page):
    login_page.login("","sdasd")
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" in url, f"Expected to remain on login page but on: {url}"
 
@pytest.mark.regression    
def test_emptypassword(login_page):
    login_page.login("anya","")
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" in url, f"Expected to remain on login page but on: {url}"

@pytest.mark.regression  
def test_emptyusernameandpassword(login_page):
    login_page.login("","")
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" in url, f"Expected to remain on login page but on: {url}"

@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.parametrize("Username,password", [
    ("anya@gmail.com", "Anya123"),
    ("", ""),
    ("anya@gmail.com", ""),
    ("", "Anya123"),
    ("anya", "Anya123"),
    ("anya@", "Anya123"),
    ("anya.com", "Anya123"),
    ("anya@gmail.com", "An1"),
    ("anya@gmail.com", "WrongPass123"),
    ("unknown_user@gmail.com", "Anya123"),
    ("ANYA@GMAIL.COM", "Anya123"),
    ("' OR 1=1 --", "anypass"),
    ("<script>alert(1)</script>", "Anya123"),
])
def test_login(login_page,Username,password):
    login_page.login(Username,password)
    url = login_page.geturl()
    assert "https://demowebshop.tricentis.com/login" in url, f"Expected to remain on login page but on: {url}"