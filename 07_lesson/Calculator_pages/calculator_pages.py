from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageCalc:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay)

class ResultCalculator:
    def __init__(self, browser):
        self._driver = browser

    def input_data(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def get_result(self):
        result_locator = (By.XPATH, '//div[@class="screen"]')
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element(result_locator, "15")
        )
        return int(self._driver.find_element(*result_locator).text)
