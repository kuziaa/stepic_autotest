from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
wait = WebDriverWait(browser, 12)

price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

btn = browser.find_element_by_css_selector("#book")
btn.click()

x_elem = browser.find_element_by_css_selector("#input_value")
x = x_elem.text

y = calc(x)

form_control = browser.find_element_by_css_selector(".form-control")
form_control.send_keys(y)

submit_button = browser.find_element_by_css_selector("#solve")
submit_button.click()



