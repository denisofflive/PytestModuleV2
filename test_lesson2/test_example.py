import time
import requests
from selenium import webdriver

class TestExample:


    def test_example(self):
        url = "https://demoqa.com/login"
        driver = webdriver.Chrome()
        driver.get(url)
        assert driver.current_url == url, "Произошёл редирект"

    def test_get_insult(self):
        response = requests.get("https://evilinsult.com/generate_insult.php")
        assert response.status_code == 200
        print(response.text)

        time.sleep(3)
