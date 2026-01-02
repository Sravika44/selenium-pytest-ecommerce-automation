import pytest
from pages.login import Login_page, Details_user, View_cart
from pages.product import product_page

def test_login(ohrm):
    user_login=Login_page(ohrm)
    user_login.click_log()

    # You can add assertions here to verify navigation to Login page
    assert ohrm.current_url.endswith("/login")
    User_details=Details_user(ohrm)
    User_details.enter_email("sravika@gmail.com")
    User_details.enter_password("Automation@25")
    User_details.click_login()

def test_cart(ohrm):
    view_cart=View_cart(ohrm)
    view_cart.click_cart()

    # You can add assertions here to verify navigation to Cart page
    assert ohrm.current_url.endswith("/view_cart")

def test_navigate_product(ohrm):
    product=product_page(ohrm)
    product.navigate_to_product()
 # You can add assertions here to verify navigation to Products page
    assert "/product_details/1" in ohrm.current_url
def test_add_to_cart_flow(ohrm):
    product = product_page(ohrm)
    product.navigate_to_product()
    product.click_add_to_cart()
    product.click_view_cart()
    product.navigate_to_products_page("Top")

    
     # You can add assertions here to verify search functionality
    assert "Top" in ohrm.page_source

def test_select_brand(ohrm):
    product = product_page(ohrm)
    product.navigate_to_products_page("Polo")
    product.select_brand()

    # You can add assertions here to verify brand selection
    assert "H&M" in ohrm.page_source  #for taking Screenshot, i failed the test intentionally by giving wrong brand name
   
@pytest.mark.smoke
def test_add_to_cart_flow(ohrm):
    product = product_page(ohrm)
    product.navigate_to_product()
    product.click_add_to_cart()

    # validation
    assert "/view_cart" in ohrm.current_url
