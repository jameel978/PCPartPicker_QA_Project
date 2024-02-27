from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Driver_instance:
    def __init__(self,driver):
        self._driver = driver

    def get_page_title(self):
        return self._driver.title

    def close_page(self):
        self._driver.close()

    def get_element_by_xpath(self, xpath):
        return self._driver.find_element(By.XPATH, xpath)

    def wait_and_get_element_by_xpath(self, xpath, sec=5):
        return WebDriverWait(self._driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def wait_and_get_elements_by_xpath(self, xpath, sec=5):
        return WebDriverWait(self._driver, sec).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def Find_and_click_on_element(self,element):
        self.wait_and_get_element_by_xpath(element).click()

    def Find_and_send_input_to_element(self,element,txt):
        self.wait_and_get_element_by_xpath(element).send_keys(txt)

    def is_element_found(self,elem,sec):
        try:
            self.wait_and_get_element_by_xpath(elem,sec=sec)
            return True
        except:
            return False


