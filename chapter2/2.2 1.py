from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(url)

num1 = browser.find_element_by_css_selector(".nowrap#num1")
num1 = int(num1.text)

num2 = browser.find_element_by_css_selector(".nowrap#num2")
num2 = int(num2.text)

sum = num2 + num1

sel = Select(browser.find_element_by_css_selector("#dropdown"))
sel.select_by_value(str(sum))

submit_btn = browser.find_element_by_css_selector(".btn-default")
submit_btn.click()
time.sleep(10)