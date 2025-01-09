from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    num1 = int(num1_element.text)  # Получаем текст и преобразуем в число
    num2 = int(num2_element.text)  # Получаем текст и преобразуем в число

    num3 = num1 + num2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(num3))

    button3 = browser.find_element(By.XPATH, '//button[contains(@type, "submit")]')
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла