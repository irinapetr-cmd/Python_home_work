from selenium.webdriver.common.by import By

class YourInformation:
    def __init__(self, driver):
        self._driver = driver

    def fill_info(self, first_name="Iris", last_name="Shu", zip_code="625042"):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self._driver.find_element(By.ID, "continue").click()
