from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button1 = browser.find_element(By.ID, "robotCheckbox")
    button1.click()

    button2 = browser.find_element(By.ID,'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()

    button3 = browser.find_element(By.XPATH, '//button[contains(@type, "submit")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла