import pytest
import sqlite3
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from faker import Faker

fake = Faker()

# @pytest.fixture(name="browser")
# def get_driver(request):
#     driver = webdriver.Chrome()
#     request.cls.driver = driver
#     yield # Передается управление тесту
#     print("После теста")
#     driver.quit()



# @pytest.fixture(name="db")
# def db_connection():
#     # Создаем соединение с базой данных
#     connection = sqlite3.connect("test.db")
#     cursor = connection.cursor()
#     # Возвращаем соединение тестам и приостанавливаем выполнение фикстуры
#     yield connection, cursor
#     print("DB Connection was closed")
#     # После завершения тестов, выполняем очистку
#     connection.close()


@pytest.fixture(autouse=True)
def get_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield # Передается управление тесту
    driver.quit()

# @pytest.fixture(autouse=True)
# def get_driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

# @pytest.fixture(scope="function")
# def print_smth():
#     login = fake.email()
#     return login

# @pytest.fixture(scope="session")
# def print_smth():
#     login = fake.email()
#     return login

# @pytest.fixture(autouse=True, scope="module")
# def print_smth():
#     login = fake.email()
#     print(login)
