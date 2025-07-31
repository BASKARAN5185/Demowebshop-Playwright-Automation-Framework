from pages.register_page import RegisterPage
import pytest

@pytest.fixture
def register_page(page):
    return RegisterPage(page)



def test_registrationform(register_page):
    register_page.navigate("https://demowebshop.tricentis.com/register")
    register_page.filltheregistrationform("male","sara","Khan","sara@gmail.com","sara@123","Sara@123")
    url=register_page.geturl()
    assert "https://demowebshop.tricentis.com/register" not in url
    
@pytest.mark.parametrize("gender,fname,lname,gmail,passw,cpass",[("Male", "John", "Doe", "john.doe@gmail.com", "password123", "password123"),
        ("Female", "Jane", "Smith", "jane.smith@gmail.com", "mypassword", "mypassword"),("","","","","","")])   
def test_registrationform(register_page,gender,fname,lname,gmail,passw,cpass):
    register_page.navigate("https://demowebshop.tricentis.com/register")
    register_page.filltheregistrationform(gender,fname,lname,gmail,passw,cpass)
    url=register_page.geturl()
    assert "https://demowebshop.tricentis.com/register" not in url

    
