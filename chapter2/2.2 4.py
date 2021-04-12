from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x_element = browser.find_element_by_css_selector("#input_value")
x = int(x_element.text)
y = calc(x)

answer_field = browser.find_element_by_css_selector(".form-control")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
answer_field.send_keys(y)

robotCheckbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
robotCheckbox.click()

robotsRule = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
robotsRule.click()

btn = browser.find_element_by_css_selector(".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
btn.click()
