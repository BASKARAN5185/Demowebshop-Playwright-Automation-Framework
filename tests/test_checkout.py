import pytest
from pages.checkout_page import CheckoutPage
from pages.cart_page import Cartpage

@pytest.fixture(scope='class')
def cart_page(page):
    cartpage = Cartpage(page)
    cartpage.navigate("https://demowebshop.tricentis.com/cart")
    cartpage.searchthequery('Science')
    cartpage.clickScienceLink()
    cartpage.clickAddToCart()
    cartpage.clickCartLink()
    return cartpage

@pytest.fixture(scope="function")
def checkoutpage(cart_page):
    checkoutpage = CheckoutPage(cart_page.page)
    checkoutpage.navigate("https://demowebshop.tricentis.com/onepagecheckout")
    yield checkoutpage

def test_valid_fillthebillingaddress(checkoutpage):
    # Fixed method name and removed argument
    if checkoutpage.selectbillingaddress():
        checkoutpage.fillthebillingaddress(
            fname='guna',
            lname='sagar',
            email='guna@gmail.com',
            company='DemoCo',
            country='India',
            state='Other (Non US)',
            city='Chennai',
            address1='north street',
            address2='avadi',
            zip='600054',
            phone='5443544554',
            faxnum='435454'
        )
    assert checkoutpage.verifythepickupinstore(), "Pickup store checkbox should be visible"

@pytest.mark.parametrize(
    "fname, lname, email, company, country, state, city, address1, address2, zip, phone, faxnum",
    [
        ("", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "Doe", "", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "", "New York", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "abcde", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "abcd", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "!@#$%", ""),
        ("<script>", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "Unknownland", "Other (Non US)", "Imaginary City", "Nowhere St", "", "00000", "0000000000", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "   ", "", "10001", "1234567890", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "123", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890123456", ""),
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New York", "123 Main St", "", "10001", "1234567890", ""),
    ]
)
def test_fillthebillingaddress(
    checkoutpage, fname, lname, email, company, country, state,
    city, address1, address2, zip, phone, faxnum
):
    # Fixed method name and removed argument
    if checkoutpage.selectbillingaddress():
        checkoutpage.fillthebillingaddress(
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

    assert not checkoutpage.verifythepickupinstore(), "Pickup store checkbox is unexpectedly visible"
