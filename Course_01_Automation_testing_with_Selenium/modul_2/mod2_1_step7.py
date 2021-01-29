from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_img_x = browser.find_element_by_id("treasure")
    x_element = find_img_x.get_attribute("valuex")
    #print(x_element)

    x = int(x_element)
    y = calc(x)
    #print(x_element, x, y)

    input_y = browser.find_element_by_id("answer")
    input_y.send_keys(y)

    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()



    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()


