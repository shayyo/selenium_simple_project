from selenium import webdriver


class MyChromeWebDriver:

    def __init__(self):
        self.driver = None
        self.web_driver_file_path = "C:/tmp/chromedriver.exe"

    def create_chrome_webdriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1680,900")
        chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(self.web_driver_file_path, chrome_options=chrome_options)
        return self.driver


class MyFirefoxWebDriver:

    def __init__(self):
        self.driver = None

    def create_firefox_webdriver(self):
        self.driver = webdriver.Firefox()
        return self.driver


class MyIeWebDriver:

    def __init__(self):
        self.driver = None

    def create_ie_webdriver(self):
        self.driver = webdriver.Ie()
        return self.driver
