import time
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path


class Test1_login:

    def test_setup(self):
        print("Test-1")
        print("Initializing driver")
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        print("Maximizing browser window")
        driver.maximize_window()

    def test_login(self):
        print("Test-2")
        print("Launching driver")
        driver.get("https://www.google.com")
        time.sleep(4)
        url = driver.current_url
        print("Navigated URL is : " + url)
        assert "Google" in driver.title

    def test_tear_down(self):
        print("Test-3")
        print("closing browser")
        driver.close()
        driver.quit()
