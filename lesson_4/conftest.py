import sqlite3
from collections import namedtuple
from selenium import webdriver
import pytest
from faker import Faker # Позволяет генерировать данные, pip3 install faker
from dataclasses import dataclass

fake = Faker()  # Через этот обьект будет генерировать данные

# @pytest.fixture()
# def connect_database():
#
#     # Установка соединения с базой данных
#     connection = sqlite3.connect('test.db')
#
#     print("Соединение с БД установлено")
#
#     # Возвращение соединения с БД
#     return connection

# @pytest.fixture
# def connect_db(request):
#     # Установка соединения с базой данных
#     connection = sqlite3.connect('test.db')
#     print("Соединение с БД установлено")
#     # Возвращение соединения с БД
#     request.cls.connection = connection

@pytest.fixture(name="driver") # Имя driver
def webdriver_init(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver

#
# @pytest.fixture
# def generate_data():
#     login = fake.email()
#     password = fake.password()
#     UserData = namedtuple('UserData', ['login', 'password'])  # именованный tuple
#     return UserData(login, password) # Возвращаем обьект


# # Определение dataclass
# @dataclass
# class UserData:
#     login: str = fake.email()
#     password: str = fake.password()
#     age: str = 13
#
#
# @pytest.fixture
# def generate_data():
#     # Генерация данных
#     login = fake.email()
#     password = fake.password()
#
#     # Возвращение объекта UserData
#     return UserData(login, password)

