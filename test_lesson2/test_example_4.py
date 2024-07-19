from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")


class TestLogin:

    def setup_method(self):
        print("Перед тестом")
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        login_field = self.driver.find_element("xpath", "//input[@id='userName']")
        login_field.send_keys("Alexey")
        assert login_field.get_attribute("value") == "Alexey", "Некорректный логин"

    def teardown_method(self):
        self.driver.quit()
        print("После теста")
