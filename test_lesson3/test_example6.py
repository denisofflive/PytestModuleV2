import pytest
import requests

from selenium import webdriver

class TestPages:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.parametrize(
        "domain, title",[
	    ("https://demoqa.com/login", "DEMOQA"), # значения domain и title для первого теста
            ("https://wikipedia.ru/", "Blank page"), # значения domain и title для второго теста
            ("https://dzen.ru/?yredirect=true", "Дзен") # значения domain и title для третьего теста
      ]
    )
    def test_open_page(self, domain, title): # Прокидываем domain и title в тест
        self.driver.get(domain)
        assert self.driver.current_url == domain, "Ошибка"
        assert self.driver.title == title, "Ошибка"

    def teardown_method(self):
        self.driver.quit()
