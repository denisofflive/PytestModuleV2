import pytest

class TestExample:

        #Прокидываем фикстуру в тест (она выполнится перед тестом)
    # def test_check_connection(self, connect_database):
    #     # Создаем курсор, чтобы делать запросы к БД
    #     cursor = connect_database.cursor()
    #
    #     # Делаем выборку из БД
    #     cursor.execute("SELECT * FROM employees")
    #
    #     # Печатаем выборку
    #     print(cursor.fetchall())
    #
    #     # Закрываем соединение с БД
    #     connect_database.close()

    # def test_login_in_account(self, generate_data):
    #     login, password = generate_data
    #     print(login, password)

    # def test_login_in_account_2(self, generate_data):
    #     print(generate_data["login"])
    #     print(generate_data["password"])

    # @pytest.mark.usefixtures("connect_db")
    # def test_login_in_account_3(self):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM employees")
    #     print(cursor.fetchall())
    #     self.connection.close()

    @pytest.mark.usefixtures("driver")  # Вызов фикстуры по заданному имени
    def test_example(self):
        self.driver.get("https://vk.com")

    # def test_example(self, generate_data):
    #     generate_data.login
    #     generate_data.password
