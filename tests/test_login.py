from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("standard_user", "secret_sauce")
    page.handle_alert_if_present()
    assert "inventory.html" in driver.current_url

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("invalid_user", "wrong_password")
    assert "Epic sadface" in page.get_error_message()