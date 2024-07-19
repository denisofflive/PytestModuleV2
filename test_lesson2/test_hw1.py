import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")


class TestLogin:

    def setup_method(self):
        print("Перед тестом")
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        username_field = self.driver.find_element("xpath", "//input[@name='username']")
        username_field.send_keys("Admin")
        print("Admin")
        password_field = self.driver.find_element("xpath", "//input[@name='password']")
        password_field.send_keys("admin123")
        print("admin123")

        assert username_field.get_attribute("value") == "Admin", "Некорректный логин"
        assert password_field.get_attribute("value") == "admin123", "Некорректный пароль"

        login_button = self.driver.find_element("xpath", "//button[@type='submit']")
        login_button.click()
        print("Click Login Button")


        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", \
            "Страница не совпадает"
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("После теста")
