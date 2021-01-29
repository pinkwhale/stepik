
# Scroll

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)

    y = calc(x)

    input_y = browser.find_element_by_id("answer")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input_y)
    input_y.send_keys(y)

    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()



finally:
    time.sleep(10)
    browser.quit()