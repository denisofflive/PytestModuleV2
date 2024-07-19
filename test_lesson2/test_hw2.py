import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")


class TestApi:

    def setup_method(self):
        print("Перед тестом")
        self.driver = webdriver.Chrome()
        self.base_url = "https://jsonplaceholder.typicode.com"

    def test_successful_request(self):
        response = requests.get(self.base_url + "/posts")
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_check_specific_entry(self):
        response = requests.get(self.base_url + "/posts/1")
        assert response.status_code == 200
        data = response.json()
        assert data["userId"] == 1
        assert data["id"] == 1

    def test_error_handling(self):
        response = requests.get(self.base_url + "/non_existent_endpoint")
        assert response.status_code != 200

    def teardown_method(self):
        self.driver.quit()
        print("После теста")
