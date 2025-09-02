import allure
import pytest
from pages.checkout_page import CheckoutPage
from pages.cart_page import Cartpage
import pytest_check as check

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

@pytest.mark.skip
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

@pytest.mark.skip
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
        ("John", "Doe", "john.doe@example.com", "OpenAI", "United States", "Other (Non US)", "New pyteYork", "123 Main St", "", "10001", "!@#$%", ""),
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

@allure.feature('Checkout the product')
@allure.story('Cash on delivery')
@allure.title('The checkout page valid cash on order')
def test_complete_checkout_flow(checkoutpage):
    # Step 1: Select or fill billing address
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

    # Step 2: Verify pickup in store is visible
    assert checkoutpage.verifythepickupinstore(), "Pickup store checkbox should be visible"

    # Step 3: Check pickup store checkbox and continue
    assert checkoutpage.checkthepickupstore(), "Failed to check pickup store checkbox"
    assert checkoutpage. clicktheshipaddresscontinebutton(), "Shipping address continue button failed"


    # Step 4: Select cash on delivery and proceed with payment
    assert checkoutpage.paymentmethod_back_and_continue_button('continue'), "Failed at payment method step"
    check.is_true(checkoutpage.visible_the_payment_info('cod'), "COD payment info not visible")
    check.is_true(checkoutpage.payment_info_back_and_continue('continue'), "Failed to continue from payment info")

    # Step 5: Validate billing info
    expected_billing_data = {
        "name": "guna sagar",
        "email": "guna@gmail.com",
        "phone": "5443544554",
        "fax": "435454",
        "address1": "north street",
        #"city_state_zip": "Chennai, 600054",  # Adjust if your UI combines these
        "country": "India"
    }
    checkoutpage.validate_billing_info(expected_billing_data)
    
    payment_and_shipping_data = {
        'Payment Method' : 'Cash On Delivery (COD)',
        'Shipping Method' :'In-Store Pickup'
    }
    checkoutpage.validate_payment_and_shiping(payment_and_shipping_data)