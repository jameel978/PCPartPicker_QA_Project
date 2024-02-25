from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class basePage:
    def __init__(self, website = "https://pcpartpicker.com/"):
        driver = webdriver.Chrome()
        driver.get(website)
        self.driver = driver


    def get_page_title(self):
        return self.driver.title

    def close_page(self):
        self.driver.close()

    def get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def wait_and_get_element_by_xpath(self, xpath, sec=2):
        return WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def wait_and_get_elements_by_xpath(self, xpath, sec=2):
        return WebDriverWait(self.driver, sec).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))