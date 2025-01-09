from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "Input your first name")]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "Input your last name")]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "Input your email")]')
    input3.send_keys("Smolensk@mail.hd")
    input4 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "Input your phone:")]')
    input4.send_keys("9999999955")
    input5 = browser.find_element(By.XPATH, '//input[contains(@placeholder, "Input your address:")]')
    input5.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[contains(@type, "submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла