import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    try:
       driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_field.clear()
        delay_field.send_keys("45")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()

        result_locator = (By.CSS_SELECTOR, ".screen")
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element(result_locator, "15"))

        result = driver.find_element(*result_locator).text
        assert result == "15", f"Ожидался результат 15, получено {result}"

    except Exception as e:
        driver.save_screenshot("calc_error.png")
        pytest.fail(f"Тест завершился с ошибкой: {str(e)}")
