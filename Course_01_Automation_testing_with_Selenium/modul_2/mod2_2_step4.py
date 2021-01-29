
from selenium import webdriver

browser = webdriver.Chrome()

#browser.execute_script('alert("Robot Works!");')
#browser.execute_script('document.title="Script executing";')

#browser.execute_script('document.title="Sript executing";alert("Robot Works!");')


link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
assert True