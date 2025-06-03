from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

input_user = driver.find_element(By.CSS_SELECTOR, "#username")
input_user.send_keys("tomsmith")
sleep(10)

input_pass = driver.find_element(By.CSS_SELECTOR, "#password")
input_pass.send_keys("SuperSecretPassword!")
sleep(10)

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()
sleep(10)

success_message =  driver.find_element(By.CSS_SELECTOR, ".flash.success")
print(success_message.text)

driver.quit()
