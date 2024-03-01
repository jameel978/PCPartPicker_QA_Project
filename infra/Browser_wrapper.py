from selenium import webdriver
from logic.helper_functions import *
class BrowserWrapper:
    def __init__(self,config_location):
        caps_list = []
        browser_configs = get_browser_config(config_location)
        test_config = get_test_config(config_location)
        for browser in browser_configs:
            browser_name = list(browser.keys())[0]
            browser_arguments = browser[browser_name][0]["argument"]
            if test_config["test_type"] == "serial":
                tmp_cap  = self.get_browser_caps_serial(browser_name,browser_arguments)
                caps_list.append((browser_name,test_config["test_type"],tmp_cap))
            elif test_config["test_type"] == "parallel":
                capabilities = browser[browser_name["capabilities"]]
                tmp_cap = self.get_browser_caps_serial(browser_name, browser_arguments, capabilities)
                caps_list.append((browser_name, test_config["test_type"], tmp_cap))
        self.caps_list = caps_list

    def get_browser_caps_serial(self,browser,arguments):
            if browser =="chrome":
                options = webdriver.ChromeOptions()
                options = self.add_browser_argument(options,arguments)
            elif browser == "edge":
                options = webdriver.EdgeOptions()
                options = self.add_browser_argument(options,arguments)
            elif browser == "firefox":
                options = webdriver.FirefoxOptions()
                options = self.add_browser_argument(options,arguments)
            else:
                return
            return options


    def get_browser_caps_parallel(self,browser,arguments,capabilities):
            if browser == "chrome":
                options = webdriver.ChromeOptions()
                options = self.add_browser_argument(options,arguments)
            elif browser == "edge":
                options = webdriver.EdgeOptions()
                options = self.add_browser_argument(options,arguments)
            elif browser == "firefox":
                options = webdriver.FirefoxOptions()
                options = self.add_browser_argument(options,arguments)
            else:
                return
            return options

    def add_browser_argument(self,options, arguments):
        for arg in arguments:
            options.add_argument(arg)
        return options

    def add_browser_argument(self,options, arguments):
        for arg in arguments:
            options.add_argument(arg)
        return options

    def get_caps(self):
        return self.caps_list