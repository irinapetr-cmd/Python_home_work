import pytest
from selenium import webdriver
from calculator_pages import MainPageCalc, ResultCalculator

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(browser):
    calc_page = MainPageCalc(browser)
    calc_page.set_delay("45")
    result_page = ResultCalculator(browser)
    result_page.input_data()
    assert result_page.get_result() == 15
