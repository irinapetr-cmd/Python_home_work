import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from OpenShop import OpenShop
from BasketShop import Basket
from CheckProductShop import CheckProduct
from YourInformation import YourInformation
from CheckResultShop import Result

@allure.feature("Магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Тест покупки товаров в магазине")
@allure.description("Проверка полного цикла покупки товаров в интернет-магазине")
def test_shop():
    with allure.step("Инициализация Firefox"):
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()))

    try:
        with allure.step("Авторизация"):
            shop_page = OpenShop(driver)
            shop_page.auth_login("standard_user")
            shop_page.auth_password("secret_sauce")
            shop_page.click_login()

        with allure.step("Добавление товаров"):
            basket = Basket(driver)
            basket.add_products()
            basket.go_to_cart()

        with allure.step("Проверка товаров"):
            check = CheckProduct(driver)
            check.verify_products()
            check.proceed_to_checkout()

        with allure.step("Заполнение информации"):
            info = YourInformation(driver)
            info.fill_info()

        with allure.step("Проверка результата"):
            result = Result(driver)
            total = result.get_total()
            assert total == "$58.29", f"Ожидалось $58.29, получено {total}"

    finally:
        with allure.step("Завершение работы"):
            driver.quit()

if __name__ == "__main__":
    test_shop()