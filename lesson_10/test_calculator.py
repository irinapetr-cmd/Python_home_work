import pytest
import allure
from selenium import webdriver
from calculator_pages import MainPageCalc, ResultCalculator


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест калькулятора с задержкой")
@allure.description("Проверка работы калькулятора с установленной задержкой вычислений")
def test_calculator(browser):
    with allure.step("Открытие калькулятора и установка задержки"):
        calc_page = MainPageCalc(browser)
        calc_page.set_delay("45")

    with allure.step("Ввод данных и получение результата"):
        result_page = ResultCalculator(browser)
        result_page.input_data()

    with allure.step("Проверка результата"):
        assert result_page.get_result() == 15, "Результат вычислений неверный"