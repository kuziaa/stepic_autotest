from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(url)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

answer_field = browser.find_element_by_css_selector("#answer")
answer_field.send_keys(y)

ch_box = browser.find_element_by_css_selector(".form-check-input[type='checkbox']")
ch_box.click()

radio = browser.find_element_by_css_selector("#robotsRule")
radio.click()

submit_btn = browser.find_element_by_css_selector(".btn-default")
submit_btn.click()
time.sleep(10)