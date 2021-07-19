from selenium import webdriver
import time
import math


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value = browser.find_element_by_id("input_value")
    value_ = int(value.text)

    fun = str(math.log(abs(12*math.sin(value_))))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(fun)

    button = browser.find_element_by_tag_name("button")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()