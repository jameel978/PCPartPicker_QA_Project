from selenium import webdriver
from Logic.helper_functions import *

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
            browser_name = list(browser.keys())[0]
            browser_arguments = browser[browser_name][0]["argument"]
            capabilities_dict = None
            if self.test_type == 'parallel':
                capabilities_dict = browser[browser_name][0]["capabilities"]
            tmp_cap = self.get_browser_cap(browser_name,browser_arguments,capabilities_dict)
            caps_list.append(tmp_cap)
        self.caps_list = caps_list

    def get_browser_cap(self,browser,arguments,capabilities_dict=None):
        options = None
        browser_webdriver = None
        if browser =="chrome":
            options = webdriver.ChromeOptions()
            options = self.add_browser_argument(options,arguments)
            browser_webdriver =  webdriver.Chrome
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            options = self.add_browser_argument(options,arguments)
            browser_webdriver = webdriver.Edge
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options = self.add_browser_argument(options,arguments)
            browser_webdriver = webdriver.Firefox
        browser_webdriver_args = {'options' : options}
        if capabilities_dict:
            #parallel run
            for key in capabilities_dict.keys():
                options.capabilities[key] = capabilities_dict[key]
            browser_webdriver = webdriver.Remote
            browser_webdriver_args = {'options' : options, 'command_executor' : self.test_HUB}
        return browser_webdriver, browser_webdriver_args

    def add_browser_argument(self,options, arguments):
        for arg in arguments:
            options.add_argument(arg)
        return options


    def get_caps(self):
        return self.caps_list