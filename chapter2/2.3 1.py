from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

btn = browser.find_element_by_css_selector("button")
btn.click()

alert = browser.switch_to.alert
alert.accept()



x_elem = browser.find_element_by_css_selector("#input_value")
x = x_elem.text

y = calc(x)

form_control = browser.find_element_by_css_selector(".form-control")
form_control.send_keys(y)

submit_btn = browser.find_element_by_css_selector(".btn")
submit_btn.click()