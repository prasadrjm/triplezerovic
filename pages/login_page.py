from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CLASS_NAME, "error-message-container")

    def load(self):
        self.driver.get(self.url)

    def open(self):
        self.driver.get(self.url)
    
    def logout(self):
        menu_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_button.click()

        logout_link = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()
    

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
    def  handle_alert_if_present(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass  # No alert found, continue

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text