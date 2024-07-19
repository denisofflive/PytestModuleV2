import time
import requests
import sqlite3
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")


class TestExample:

    def setup_method(self):
        self.connection = sqlite3.connect("../db.sqlite")
        self.cursor = self.connection.cursor()

    def test_db_example(self):
        users = self.cursor.execute("select * from users")
        # print(users.fetchone())
        assert "Alice" in users.fetchone()

    def teardown_method(self):
        self.connection.close()
