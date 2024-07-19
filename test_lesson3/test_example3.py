import time
import pytest
from selenium import webdriver

class TestPages: # Название тестового класса

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.parametrize("url", open("urls.txt").readlines())
    def test_open_pages(self, url):
        clear_url = f"{url.strip()}"
        self.driver.get(clear_url)
        assert self.driver.current_url == clear_url, "Ошибка"

    def teardown_method(self):
        self.driver.quit()
