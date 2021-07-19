from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button.click()

    value = browser.find_element_by_id("input_value")
    value_ = int(value.text)

    fun = str(math.log(abs(12*math.sin(value_))))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(fun)

    button2 = browser.find_element_by_id("solve")
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()