from pages.checkout_page import CheckoutPage
from playwright.async_api import Playwright
import pytest


@pytest.fixture(scope="class")
def browesr(page):
    checkoutpage=CheckoutPage(page)
    checkoutpage.navigate("https://demowebshop.tricentis.com/onepagecheckout")
    yield checkoutpage
    
@pytest.mark.smoke
@pytest.mark.regression
def test_fill_the_Billing_address(browesr):
    browesr.fillthebillingaddress('guna','sagar','guna@gmail.com','India','1','Chennai','north street','avadi','600054','5443544554','435454')   


@pytest.mark.regression
@pytest.mark.parametrize(
    "fname, lname, email, company, country, state, city, address1, address2, zip, phone, faxnum",
    [
        # ❌ INVALID CASES (19)
        ("", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "1234567890", ""),  # Missing first name
        ("John", "", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "1234567890", ""),  # Missing last name
        ("John", "Doe", "", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "1234567890", ""),                   # Missing email
        ("John", "Doe", "john.doe@", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "1234567890", ""),          # Invalid email format
        ("John", "Doe", "john.doe@example.com", "OpenAI", "", "1", "New York", "123 Main St", "", "10001", "1234567890", ""),            # Missing country
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "", "New York", "123 Main St", "", "10001", "1234567890", ""),# Missing state
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "", "123 Main St", "", "10001", "1234567890", ""),       # Missing city
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "", "", "10001", "1234567890", ""),          # Missing address1
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "", "1234567890", ""),    # Missing zip
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "", ""),         # Missing phone
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "abcde", "1234567890", ""), # Invalid zip
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "abcd", ""),     # Invalid phone
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "!@#$%", ""),    # Special chars in phone
        ("<script>", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "1234567890", ""),  # Script in fname
        ("John", "Doe", "john.doe@example.com", "OpenAI", "Unknownland", "99", "Imaginary City", "Nowhere St", "", "00000", "0000000000", ""), # Invalid country/state
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "   ", "", "10001", "1234567890", ""),        # Address1 only whitespace
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "123", ""),       # Phone too short
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "1", "New York", "123 Main St", "", "10001", "1234567890123456", ""),  # Phone too long
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "NaN", "New York", "123 Main St", "", "10001", "1234567890", ""),  # Non-numeric state
    ]
)
def test_fill_the_billing_address(
    browser, fname, lname, email, company, country, state,
    city, address1, address2, zip, phone, faxnum
):
    browser.fillthebillingaddress(
        fname=fname,
        lname=lname,
        email=email,
        company=company,
        country=country,
        state=state,
        city=city,
        address1=address1,
        address2=address2,
        zip=zip,
        phone=phone,
        faxnum=faxnum
    )
    assert browser.verifythepickupinstore() in False, "Pickup store checkbox is visible"
    

    

