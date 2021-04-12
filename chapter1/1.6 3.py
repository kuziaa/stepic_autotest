from selenium import webdriver
import time


url = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(url)

fields = browser.find_elements_by_css_selector('[type="text"]')
for field in fields:
    field.send_keys("xxx")

submit_btn = browser.find_element_by_css_selector('[type="submit"]')
submit_btn.click()
time.sleep(10)