import time

import pytest
import os

from selenium import webdriver

class TestPages:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.parametrize(
    "path_to_file",
      [
        (f"{os.getcwd()}/uploads/document.doc"),
        (f"{os.getcwd()}/uploads/image.jpg"),
        (f"{os.getcwd()}/uploads/music.mp3"),
      ]
    )
    def test_file_upload(self, path_to_file):
        self.driver.get("http://the-internet.herokuapp.com/upload")
        self.driver.find_element("xpath", "//input[@type='file']").send_keys(path_to_file)
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

