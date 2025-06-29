from selenium.webdriver.common.by import By

class Result:
    def __init__(self, driver):
        self._driver = driver

    def get_total(self):
        return self._driver.find_element(By.CLASS_NAME, "summary_total_label").text.split()[-1]