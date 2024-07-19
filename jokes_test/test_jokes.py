import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BUZZ_LINK_LOCATOR = ("xpath", "//span[text()='Buzz']")
POST_TEXTAREA_LOCATOR = ("xpath", "//textarea[@class='oxd-buzz-post-input']")
POST_BUTTON_LOCATOR = ("xpath", "//button[@type='submit']")
POSTED_JOKE_LOCATOR = ("xpath", "//div[@class='orangehrm-buzz-post-body']")


def test_post_joke(get_joke, open_browser, login):
    driver = open_browser
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
    buzz_link = (WebDriverWait(driver, 10).
                 until(EC.presence_of_element_located(BUZZ_LINK_LOCATOR)))
    buzz_link.click()

    post_textarea = (WebDriverWait(driver, 10).
                     until(EC.presence_of_element_located(POST_TEXTAREA_LOCATOR)))
    post_textarea.send_keys(get_joke)
    print(get_joke)
    post_button = (WebDriverWait(driver, 10).
                   until(EC.presence_of_element_located(POST_BUTTON_LOCATOR)))
    post_button.click()
    time.sleep(3)
    posted_joke = (WebDriverWait(driver, 10).
                   until(EC.presence_of_element_located(POSTED_JOKE_LOCATOR)).text)
    print(posted_joke)
    posted_joke = get_joke
    assert get_joke in posted_joke
