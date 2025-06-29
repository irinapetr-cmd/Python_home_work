from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageCalc:
    def __init__(self, browser):
        """Инициализация страницы калькулятора.

        Args:
            browser: WebDriver - экземпляр веб-драйвера
        """
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay: str) -> None:
        """Установка задержки вычислений.

        Args:
            delay: str - значение задержки в секундах
        """
        delay_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay)


class ResultCalculator:
    def __init__(self, browser):
        """Инициализация страницы с результатами калькулятора.

        Args:
            browser: WebDriver - экземпляр веб-драйвера
        """
        self._driver = browser

    def input_data(self) -> None:
        """Ввод данных для вычисления: 7 + 8."""
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def get_result(self) -> int:
        """Получение результата вычислений.

        Returns:
            int: результат вычислений
        """
        result_locator = (By.XPATH, '//div[@class="screen"]')
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element(result_locator, "15")
        )
        return int(self._driver.find_element(*result_locator).text)