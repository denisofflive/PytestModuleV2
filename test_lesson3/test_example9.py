import pytest

class TestDependency:

    @pytest.mark.dependency(name="test_1")
    def test_1(self):  # Тест упадет
        assert False

    @pytest.mark.dependency(name="test_2", depends=["test_1"])  # Зависимость от test_1
    def test_2(self):  # Тест не запуститься, так как test_1 упадет
        assert True
