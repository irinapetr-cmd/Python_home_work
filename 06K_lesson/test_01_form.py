import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button.btn-outline-primary").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))
    )

    field_zip = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "alert-danger" in field_zip

    fields_to_check = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "company"
    ]

    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} не подсвечено зеленым"
