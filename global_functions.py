from class_webdrivers import MyChromeWebDriver, MyFirefoxWebDriver, MyIeWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_web_driver(requested_web_driver_type="Chrome"):
    """Ask for a webdriver: 'Chrome', 'Firefox' 'Ie'
    where 'Chrome is the default' """

    if requested_web_driver_type == "Chrome":
        requested_web_driver_type = MyChromeWebDriver().create_chrome_webdriver()
    elif requested_web_driver_type == "Firefox":
        requested_web_driver_type = MyFirefoxWebDriver().create_firefox_webdriver()
    elif requested_web_driver_type == "Ie":
        requested_web_driver_type = MyIeWebDriver().create_ie_webdriver()
    else:
        print("No such web driver exits '" + requested_web_driver_type + "'\n")
        exit(53)
    return requested_web_driver_type
