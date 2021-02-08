
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_basket_is_on_page(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
