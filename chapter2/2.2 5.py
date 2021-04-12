import os
from selenium import webdriver



browser = webdriver.Chrome()
url = "http://suninjuly.github.io/file_input.html"
browser.get(url)


first_name = browser.find_element_by_css_selector(".form-control[name='firstname']")
first_name.send_keys('xxx')

last_name = browser.find_element_by_css_selector(".form-control[name='lastname']")
last_name.send_keys('xxx')

email = browser.find_element_by_css_selector(".form-control[name='email']")
email.send_keys('xxx')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '111.txt')           # добавляем к этому пути имя файла
send_file = browser.find_element_by_css_selector("[type='file']")
send_file.send_keys(file_path)

submit_btn = browser.find_element_by_css_selector(".btn")
submit_btn.click()