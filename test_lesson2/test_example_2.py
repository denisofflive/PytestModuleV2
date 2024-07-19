import time
import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

class TestExample:

    def setup_method(self):
        print("Перед тестом")
        self.driver = webdriver.Chrome()

    def test_example(self):
        url = "https://demoqa.com/login"
        self.driver.get(url)
        assert self.driver.current_url == url, "Произошёл редирект"

    def test_example_2(self):
        url = "https://demoqa.com/links"
        self.driver.get(url)
        assert self.driver.current_url == url, "Произошёл редирект"

    def teardown_method(self):
        self.driver.quit()
        print("После теста")

        time.sleep(3)
