from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(url)

people_radio = browser.find_element_by_css_selector("#peopleRule")
people_checked = people_radio.get_attribute("checked")
print(people_checked)
robot_radio = browser.find_element_by_css_selector("#robotsRule")
robot_checked = robot_radio.get_attribute("checked")
print(robot_checked)

time.sleep(10)