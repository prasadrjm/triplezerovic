import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_argument("--start-maximized")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")  # Incognito mode disables autofill

    # Disable autofill and password manager features explicitly
    options.add_argument("--disable-features=AutofillServerCommunication,PasswordManagerEnableMigrationToAccountStore,AutofillEnableAccountWalletStorage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    # driver.quit()