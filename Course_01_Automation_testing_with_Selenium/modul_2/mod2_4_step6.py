from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#link = " http://suninjuly.github.io/cats.html"
link = "http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
#    browser.implicitly_wait(5)
    browser.get(link)

    button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, 'verify'))
    )
    #button = browser.find_element_by_id("button")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:

    browser.quit()




