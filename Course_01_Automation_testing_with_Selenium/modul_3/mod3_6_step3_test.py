
import pytest
from selenium import webdriver

import math
import time

link_list = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

final = ""

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser')
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print('\nquit browser')
    browser.quit()
    print(final)

@pytest.mark.parametrize("link_list", link_list)
def test_task(browser, link_list):
    browser.get(link_list)
    global final
    answer = str(math.log(int(time.time())))
    input_y = browser.find_element_by_css_selector('.textarea')
    input_y.send_keys(answer)

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    message = browser.find_element_by_css_selector(".smart-hints__hint")
    #print(message.text)
    try:
        assert "Correct!" in message.text, 'message not equal "Correct!"'
    except AssertionError:
        final += message.text

