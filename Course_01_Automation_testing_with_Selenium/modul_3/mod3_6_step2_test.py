
import pytest
from selenium import webdriver

#link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope='function')
def browser():
    print('\nstart browser..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()

@pytest.mark.parametrize('language', ['ru', 'en-gb'])
def test_quest_should_see_login_link(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/'
    browser.get(link)
    browser.find_element_by_css_selector('#login_link')


