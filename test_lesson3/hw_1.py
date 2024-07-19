import pytest
from selenium import webdriver

class TestExample:

    USERNAME_FIELD_LOCATOR = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//input[@id='login-button']")
    ERROR_BUTTON = ("xpath", "//h3[@data-test='error']")

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    @pytest.mark.parametrize(
        "email, password, error_message, expected_result", [
            # Позитивный тест-кейс
            ("standard_user", "secret_sauce", None, True),
            # Негативные тест-кейсы
            ("gwrrfdsa.ru", "secret_sauce", "Epic sadface: Username and password do not match any user in this service",
             False),
            ("standard_user", "", "Epic sadface: Password is required", False),
            ("", "secret_sauce", "Epic sadface: Username is required", False),
            ("", "", "Epic sadface: Username is required", False),
        ]
    )
    def test_login(self, email, password, error_message, expected_result):
        driver = self.driver
        driver.find_element(*self.USERNAME_FIELD_LOCATOR).send_keys(email)
        driver.find_element(*self.PASSWORD_FIELD_LOCATOR).send_keys(password)
        driver.find_element(*self.LOGIN_BUTTON_LOCATOR).click()

        if expected_result == False:
            assert driver.find_element(*self.ERROR_BUTTON).text == error_message

        # if expected_result == False:
        #     self.driver.find_element(*self.ERROR_BUTTON).is_displayed()
        # else:
        #     assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    def teardown_method(self):
        self.driver.quit()
