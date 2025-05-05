import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By

@pytest.mark.logout
def test_logout(driver):
    # 1. Log in to the application
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Assert successful login by checking a unique element visible only after login
    assert driver.find_element(By.ID, "inventory_container").is_displayed()

    # 2. Log out of the application
    login_page = LoginPage(driver)
    login_page.logout()
    login_page.handle_alert_if_present()

    # # 3. Assert that the login page is visible after logout
    # assert login_page.is_login_page_visible()
