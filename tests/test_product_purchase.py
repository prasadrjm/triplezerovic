import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

# @pytest.mark.product_purchase
def test_product_purchase(driver):
    # 1. Log in to the application
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # Assert successful login by checking a unique element visible only after login
    assert driver.find_element(By.ID, "inventory_container").is_displayed()

    # 2. Add a product to the cart
    product_page = ProductPage(driver)
    product_page.add_product_to_cart("Sauce Labs Backpack")
    
    # Assert product added to the cart
    assert product_page.cart_count() == 1

    # 3. Proceed to checkout
    product_page.go_to_cart()
    cart_page = CartPage(driver)
    cart_page.checkout()

    # 4. Fill in the checkout form and complete the purchase
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("John", "Doe", "12345")
    checkout_page.finish_checkout()

    # 5. Assert successful purchase by checking the confirmation message
    confirmation_text = checkout_page.get_confirmation_message()
    assert confirmation_text == "Thank you for your order!"
