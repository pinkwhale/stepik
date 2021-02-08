
import unittest
from selenium import webdriver
import time

class TestRegForms(unittest.TestCase):
    def test_reg_form1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_class [placeholder*='name']")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector(".second_class [placeholder*='name']")
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector(".third_class [placeholder*='email']")
        input3.send_keys("petrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text
        #self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error")
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        #time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_reg_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_class [placeholder*='name']")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_css_selector(".second_class [placeholder*='name']")
        input2.send_keys("Petrov")

        input3 = browser.find_element_by_css_selector(".third_class [placeholder*='email']")
        input3.send_keys("petrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text



        # ожидание чтобы визуально оценить результаты прохождения скрипта
        #time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "welcome_text is not delivered")


if __name__ == "__main__":
    unittest.main()

