import time
import pytest
from selenium import webdriver

class TestPages: # Название тестового класса

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.parametrize(
        "url", [
            "https://demoqa.com/login",
            "https://demoqa.com/books",
            "https://demoqa.com/profile"
        ]
    )
    def test_open_pages(self, url):
        self.driver.get(url)
        assert self.driver.current_url == url, "Ошибка"

    def teardown_method(self):
        self.driver.quit()
