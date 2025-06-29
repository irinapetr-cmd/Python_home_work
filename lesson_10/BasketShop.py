from selenium.webdriver.common.by import By


class Basket:
    def __init__(self, driver):
        """Инициализация корзины магазина.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self._driver = driver

    def add_products(self) -> None:
        """Добавление товаров в корзину."""
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self) -> None:
        """Переход в корзину."""
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()