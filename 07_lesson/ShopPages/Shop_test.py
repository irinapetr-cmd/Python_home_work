from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from OpenShop import OpenShop
from BasketShop import Basket
from CheckProductShop import CheckProduct
from YourInformation import YourInformation
from CheckResultShop import Result


def test_shop():
    # Инициализация Firefox
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

    try:
        # 1. Авторизация
        shop_page = OpenShop(driver)
        shop_page.auth_login("standard_user")
        shop_page.auth_password("secret_sauce")
        shop_page.click_login()

        # 2. Добавление товаров
        basket = Basket(driver)
        basket.add_products()
        basket.go_to_cart()

        # 3. Проверка товаров
        check = CheckProduct(driver)
        check.verify_products()
        check.proceed_to_checkout()

        # 4. Заполнение информации
        info = YourInformation(driver)
        info.fill_info()

        # 5. Проверка результата
        result = Result(driver)
        total = result.get_total()

        assert total == "$58.29", f"Ожидалось $58.29, получено {total}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shop()
