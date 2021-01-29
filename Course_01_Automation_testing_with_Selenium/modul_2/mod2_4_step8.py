
# Wait by WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button = browser.find_element(By.ID, 'book')
    button.click()

    x_element = browser.find_element_by_id("input_value")
    browser.execute_script('return arguments[0].scrollIntoView(true);', x_element)
    x = int(x_element.text)

    y = calc(x)

    input_y = browser.find_element_by_id("answer")
    input_y.send_keys(y)

    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()

