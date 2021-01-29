from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")


try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Ivan")

    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Petrov")

    email = browser.find_element_by_name("email")
    email.send_keys("ivan_petrov@mail.ru")

    file_element = browser.find_element_by_id("file")
    file_element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


