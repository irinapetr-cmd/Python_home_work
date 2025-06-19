from selenium.webdriver.common.by import By

class OpenShop:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def auth_login(self, login):
        self._driver.find_element(By.ID, "user-name").send_keys(login)

    def auth_password(self, password):
        self._driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self._driver.find_element(By.ID, "login-button").click()
