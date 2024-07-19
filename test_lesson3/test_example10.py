import pytest
from selenium import webdriver

class TestExample:

    EMAIL_FIELD_LOCATOR = ("xpath", "//input[@id='login_email']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON_LOCATOR = ("xpath", "//button[@id='loginformsubmit']")
    TERMS_CHECKBOX = ("xpath", "(//input[@class='remember'])[1]")
    ERROR_LABEL = ("xpath", "//span[contains(@class, 'error')]//li")

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.freeconferencecall.com/login")

    @pytest.mark.parametrize(
        "email, password, error_message, expected_result", [
            # Позитивный тест-кейс
            ("demoqa@ya.ru", "123", None, True),
            # Негативные тест-кейсы
            ("gwrrfdsa.ru", "123", "Введите адрес электронной почты", False),
            ("demoqa@ya.ru", "", "Обязательное поле", False),
            ("", "123", "Введите адрес электронной почты", False),
            ("", "", "Обязательное поле", False),
        ]
    )
    def test_login(self, email, password, error_message, expected_result):
        driver = self.driver
        driver.find_element(*self.EMAIL_FIELD_LOCATOR).send_keys(email)
        driver.find_element(*self.PASSWORD_FIELD_LOCATOR).send_keys(password)
        driver.find_element(*self.TERMS_CHECKBOX).click()
        driver.find_element(*self.SUBMIT_BUTTON_LOCATOR).click()
        # if expected_result:
        #     assert driver.find_element(*self.ERROR_LABEL).text == error_message
        # if not expected_result:
        #     assert driver.find_element(*self.ERROR_LABEL).text == error_message
        if expected_result == False:
            self.driver.find_element(*self.ERROR_LABEL).is_displayed()

    def teardown_method(self):
        self.driver.quit()
