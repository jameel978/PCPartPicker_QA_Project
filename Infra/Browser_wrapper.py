from selenium import webdriver
from Logic.Utils import *

class BrowserWrapper:
    def __init__(self,config_location = None):
        caps_list = []
        self.test_type = None
        browser_configs = None
        if config_location:
            browser_configs = get_browser_config(config_location)
            test_config = get_test_config(config_location)
            self.test_type = test_config["test_type"] # serial/parallel
            self.test_HUB = test_config["HUB"]
            
        for browser in browser_configs:
            tmp_cap = self.get_browser_cap(browser)
            caps_list.append(tmp_cap)
        self.caps_list = caps_list

    def get_browser_cap(self,browser):
        options = None
        browser_webdriver = None
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            browser_webdriver = webdriver.Chrome
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            browser_webdriver = webdriver.Edge
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            browser_webdriver = webdriver.Firefox
        # Adding argument to disable the AutomationControlled flag
        options.add_argument("--disable-blink-features=AutomationControlled")
        # Exclude the collection of enable-automation switches
        if browser != "firefox":
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # Turn-off userAutomationExtension
            options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--start-maximized")
        browser_webdriver_args = {'options' : options}
        if self.test_type == "parallel":
            options.capabilities["platformName"] = "Windows 11"
            browser_webdriver = webdriver.Remote
            browser_webdriver_args = {'options' : options, 'command_executor': self.test_HUB}
        return browser_webdriver, browser_webdriver_args


    def get_caps(self):
        return self.caps_list