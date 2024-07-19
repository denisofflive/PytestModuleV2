import time
import pytest


class TestExample:

    # Один параметр
    @pytest.mark.parametrize("number", [1, 2, 3])
    def test_numbers(self, number):
        print(number)

    # Два параметра
    @pytest.mark.parametrize(
        "login, password", [
        ("manikosto", "123456789"),
        ("denisov", "987654321")
        ]
    )
    def test_login_user(self, login, password):
        print(f"Логин: {login}, Пароль: {password}")
