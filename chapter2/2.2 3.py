from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_css_selector(".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
