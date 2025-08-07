from pages.register_page import RegisterPage
import pytest

@pytest.fixture
def register_page(page):
    return RegisterPage(page)

@pytest.mark.register 
@pytest.mark.smoke
def test_registrationform(register_page):
    register_page.navigate("https://demowebshop.tricentis.com/register")
    register_page.filltheregistrationform("male","sara","Khan","sara@gmail.com","sara@123","Sara@123")
    url=register_page.geturl()
    assert "https://demowebshop.tricentis.com/register" not in url

@pytest.mark.regression
@pytest.mark.register    
@pytest.mark.parametrize("gender,fname,lname,gmail,passw,cpass", [
    ("", "", "", "", "", ""),
    ("Male", "", "Doe", "john.doe@gmail.com", "Password123!", "Password123!"),
    ("Female", "Jane", "", "jane.smith@gmail.com", "MyPassw0rd!", "MyPassw0rd!"),
    ("Male", "John", "Doe", "", "Password123!", "Password123!"),
    ("Male", "John", "Doe", "john.doe@gmail.com", "", ""),
    
    # ❌ Invalid email formats
    ("Male", "John", "Doe", "john.doegmail.com", "Password123!", "Password123!"),
    ("Female", "Jane", "Smith", "jane.smith@", "MyPassw0rd!", "MyPassw0rd!"),
    ("Male", "John", "Doe", "john@.com", "Password123!", "Password123!"),

    # ❌ Password mismatch
    ("Male", "John", "Doe", "john.doe@gmail.com", "Password123!", "WrongPass123!"),

    # ❌ Weak passwords
    ("Female", "Anna", "Lee", "anna.lee@gmail.com", "123", "123"),
    ("Male", "Mark", "Zee", "mark.zee@gmail.com", "password", "password"),
    ("Female", "Sara", "Connor", "sara.connor@gmail.com", "abcdefg", "abcdefg"),

    # ✅ Edge cases (long names, special characters)
    ("Male", "A" * 50, "B" * 50, "long.name@example.com", "LongPassword123$", "LongPassword123$"),
    ("Female", "Élise", "Dubois", "elise.dubois@example.fr", "ÉlitePass99!", "ÉlitePass99!"),  ])   
def test_registrationform(register_page,gender,fname,lname,gmail,passw,cpass):
    register_page.navigate("https://demowebshop.tricentis.com/register")
    register_page.filltheregistrationform(gender,fname,lname,gmail,passw,cpass)
    assert "https://demowebshop.tricentis.com/register" in register_page.page.url

    
