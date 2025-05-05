from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        product = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']/descendant::button")
        product.click()

    def cart_count(self):
        return int(self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
