from selenium.webdriver.common.by import By

class CheckProduct:
    def __init__(self, driver):
        self._driver = driver

    def verify_products(self):
        products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for product in products:
            self._driver.find_element(By.XPATH, f'//div[text()="{product}"]')

    def proceed_to_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()