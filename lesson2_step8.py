from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys('Ivan')

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys('Ivanov')

    email = browser.find_element_by_name("email")
    email.send_keys('example@mail.ru')

    file_button = browser.find_element_by_css_selector("[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '2_8.txt')  
    file_button.send_keys(file_path)
    

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