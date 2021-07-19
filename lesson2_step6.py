from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math


try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element_by_id("input_value")
    value_ = int(value.text)

    fun = str(math.log(abs(12*math.sin(value_))))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(fun)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    button = browser.find_element_by_tag_name("button")
    option2 = browser.find_element_by_id("robotsRule")

    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)

    option2.click()
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()