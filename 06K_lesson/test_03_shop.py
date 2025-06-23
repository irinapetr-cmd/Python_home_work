import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_shopping(driver):

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Elena")
    driver.find_element(By.ID, "last-name").send_keys("Petrova")
    driver.find_element(By.ID, "postal-code").send_keys("310510")
    driver.find_element(By.ID, "continue").click()

    result = driver.find_element(
        By.CSS_SELECTOR, "[data-test='total-label']").text
    total = result.replace("Total: $", "").strip()

    assert total == "58.29", f"Ожидалась сумма $58.29, получено ${total}"
