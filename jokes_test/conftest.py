import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

USERNAME_FIELD_LOCATOR = ("xpath", "//input[@name='username']")
PASSWORD_FIELD_LOCATOR = ("xpath", "//input[@name='password']")
LOGIN_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")


@pytest.fixture
def get_joke():
    response = requests.get("https://geek-jokes.sameerkumar.website/api")
    yield response.text


@pytest.fixture(scope="function")
def open_browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(open_browser):
    driver = open_browser
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    username_field = (WebDriverWait(driver, 10).
                      until(EC.presence_of_element_located(USERNAME_FIELD_LOCATOR)))
    username_field.send_keys("Admin")
    password_field = (WebDriverWait(driver, 10).
                      until(EC.presence_of_element_located(PASSWORD_FIELD_LOCATOR)))
    password_field.send_keys("admin123")
    login_button = (WebDriverWait(driver, 10).
                    until(EC.presence_of_element_located(LOGIN_BUTTON_LOCATOR)))
    login_button.click()
