from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element_by_id("num1")
    n1_ = int(n1.text)

    n2 = browser.find_element_by_id("num2")
    n2_ = int(n2.text)

    summa = str(n1_ + n2_)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()