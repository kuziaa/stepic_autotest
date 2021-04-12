from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")
time.sleep(10)