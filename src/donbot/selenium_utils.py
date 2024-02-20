from selenium import webdriver


class SeleniumUtils:
    def __init__(self, driver_path):
        """
        Initialize SeleniumUtils with the path to the Chrome driver.

        :param driver_path: Path to the Chrome driver executable.
        """
        self.driver = webdriver.Chrome(driver_path)

    def open_url(self, url):
        self.driver.get(url)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def close(self):
        self.driver.quit()
