
# New Tab

from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.trollface')
    button.click()

    new_tab = browser.window_handles[1]

    browser.switch_to.window(new_tab)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    y = calc(x)

    input_y = browser.find_element_by_id("answer")
    input_y.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

