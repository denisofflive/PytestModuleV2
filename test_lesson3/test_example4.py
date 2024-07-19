import time
import pytest
import requests
class TestPages: # Название тестового класса

    @pytest.mark.parametrize("url", open("urls.txt").readlines())
    def test_open_pages(self, url):
        clear_url = f"{url.strip()}"
        response = requests.get(clear_url)
        assert response.status_code == 200, "Ошибка"
