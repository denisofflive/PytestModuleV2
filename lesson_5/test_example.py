import time

import pytest


class TestExample:
    # @pytest.mark.usefixtures("browser")  # Вызов фикстуры по заданному имени
    # def test_example(self):
    #     self.driver.get("https://vk.com")


    # def test_example2(self, db):
    #     # cursor = db[1]
    #     connection, cursor = db
    #     cursor.execute("SELECT * FROM employees")
    #     print(cursor.fetchall())

    @pytest.mark.smoke
    def test_example3(self):
        self.driver.get("https://vk.com")
        time.sleep(1)

    @pytest.mark.smoke
    def test_example4(self):
        self.driver.get("https://www.rambler.ru/")
        time.sleep(1)

    @pytest.mark.smoke
    def test_example5(self):
        self.driver.get("https://www.mail.ru/")
        time.sleep(1)
#
#     def test_example4(self):
#         print("123")
#
# class TestExample2:
#
#     def test_example5(self):
#         print("123")

    # def test_example6(self):
    #     print("123")