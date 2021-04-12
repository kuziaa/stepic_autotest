from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(url)

treasure = browser.find_element_by_css_selector("#treasure")
x = treasure.get_attribute("valuex")
y = calc(x)

answer_field = browser.find_element_by_css_selector("#answer")
answer_field.send_keys(y)

ch_box = browser.find_element_by_css_selector(".check-input[type='checkbox']")
ch_box.click()

radio = browser.find_element_by_css_selector("#robotsRule")
radio.click()

submit_btn = browser.find_element_by_css_selector(".btn-default")
submit_btn.click()
time.sleep(10)