from selenium.webdriver.common.by import By
from infra.base_page import basePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class PC_PART_PICKER(basePage):
    LOGIN_BUTTON_XPATH = "//ul[@class='nav__account nav__account--desktop list-unstyled']/li[@class='nav__account--login']"
    USER_INPUT = "//input[@id='id_username']"
    PASSWORD_INPUT = "//input[@id='id_password']"
    SUBMIT_BUTTON = "//input[@id='input_recaptcha']"

    def __init__(self):
        super().__init__()

    def wait_and_get_element_by_xpath(self,xpath,sec=2):
        return WebDriverWait(self.driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)) )

    def fill_username_input(self,username):
        self.user_input = self.wait_and_get_element_by_xpath(self.USER_INPUT)
        self.user_input.send_keys(username)
    def fill_password_input(self, password):
        self.password_input = self.wait_and_get_element_by_xpath(self.PASSWORD_INPUT)
        self.password_input.send_keys(password)
    def click_on_login_submit_button(self):
        self.submit_button = self.wait_and_get_element_by_xpath(self.SUBMIT_BUTTON)
        self.submit_button.click()

    def click_on_login_button(self):
        self.login_button = self.wait_and_get_element_by_xpath(self.LOGIN_BUTTON_XPATH)
        self.login_button.click()

    def login_flow(self,username,password):
        self.click_on_login_button()
        self.fill_username_input(username)
        self.fill_password_input(password)
        self.click_on_login_submit_button()