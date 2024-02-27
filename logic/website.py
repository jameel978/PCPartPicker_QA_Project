from selenium.webdriver.common.by import By
from infra.base_page import basePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class PC_PART_PICKER(basePage):
    #HOMEPAGE
    #https://pcpartpicker.com/
    LOGIN_BUTTON_XPATH = "//ul[@class='nav__account nav__account--desktop list-unstyled']/li[@class='nav__account--login']"
    START_BUILDING_YOUR_PC_BUTTON = "//a[normalize-space()='Start Your Build']"
    BUILDER_BUTTON = "//ul[@role='presentation']//li[@class='nav__categories--partlist']"
    PRODUCT_BUTTON = "//a[contains(text(),'Products')]"
    GUIDES_BUTTON = "//ul[@role='presentation']//li[@class='nav__categories--guides']"
    COMPLETE_BUILDS_BUTTON = "//a[contains(text(),'Completed Builds')]"
    TRENDS_BUTTON = "//a[contains(text(),'Trends')]"
    FOURMS_BUTTON = "//a[contains(text(),'Forums')]"
    
    #AFTER LOGIN_BUTTON
    LOGOUT_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--logout']//a[normalize-space()='Log Out']"
    SAVED_PARTS_BUTTON = "//ul[@role='presentation']//a[contains(text(),'Saved Parts Lists')]"
    FAVORITE_PART_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--favorites']//a[contains(text(),'Favorite Parts')]"
    
    #BUILDPCSECTION
    #https://pcpartpicker.com/list/
    CHOOSE_CPU = "//a[normalize-space()='CPU']"
    CHOOSE_CPU_COOLER = "//a[normalize-space()='CPU']"
    CHOOSE_MOTHERBOARD = "//a[normalize-space()='Motherboard']"
    CHOOSE_MEMORY = "//td[contains(@class,'td__component')]//a[normalize-space()='Memory']"
    CHOOSE_STORAGE = "//td[contains(@class,'td__component')]//a[normalize-space()='Storage']"
    CHOOSE_GPU = "//td[contains(@class,'td__component')]//a[normalize-space()='Video Card']"
    CHOOSE_CASE = "//a[normalize-space()='Case']"
    CHOOSE_PSU = "//a[normalize-space()='Power Supply']"
    CHOOSE_OS = "//a[normalize-space()='Operating System']"
    CHOOSE_MONITOR = "//a[normalize-space()='Monitor']"
    
    #PRODUCT_PAGE
    #https://pcpartpicker.com/products/
    CPU_PAGE = "//ul[@class='inside']//a[normalize-space()='CPUs']"
    CPU_COOLER_PAGE = "//ul[@class='inside']//a[normalize-space()='CPU Coolers']"
    MOBO_PAGE = "//ul[@class='inside']//a[normalize-space()='Motherboards']"
    RAM_PAGE = "//ul[@class='inside']//a[normalize-space()='Memory']"
    STORAGE_PAGE = "//ul[@class='inside']//a[normalize-space()='Storage']"
    GPU_PAGE = "//ul[@class='inside']//a[normalize-space()='Video Cards']"
    CASES_PAGE = "//ul[@class='inside']//a[normalize-space()='Cases']"
    PSU_PAGE = "//ul[@class='inside']//a[normalize-space()='Power Supplies']"
    OS_PAGE = "//ul[@class='inside']//a[normalize-space()='Operating Systems']"
    MONITOR_PAGE = "//ul[@class='inside']//a[normalize-space()='Monitors']"
    
    #LOGIN_PAGE
    USER_INPUT = "//input[@id='id_username']"
    PASSWORD_INPUT = "//input[@id='id_password']"
    SUBMIT_BUTTON = "//input[@id='input_recaptcha']"
    
    #REGISTRATION_PAGE
    EMAIL_INPUT = "//input[@id='id_email']"
    EMAIL_INPUT_SECOND = "//input[@id='id_email2']"
    PASSWORD_INPUT_SECOND = "//input[@id='id_password1']"
    ACCEPT_TOS_CHECKBOX = "//input[@id='id_accept_tos']"
    ACCEPT_UCOC_CHECKBOX = "//input[@id='id_accept_ucoc']"
    
    GEBERAL_TEXT_ERROE = "//p[@class='text-error']"
    ALREADY_REGISTERED_USERNAME = "//p[normalize-space()='A user with that username already exists.']   "
    IVALID_USERNAME = "//p[contains(text(),'This value may contain only letters, numbers and @')]"
    ALREADY_REGISTERED_EMAIL = "//p[contains(text(),'This email address is already in use. Please suppl')]"
    NOT_MATHCING_EMAIL = '(//p[normalize-space()="The two email fields didn\'t match."])'
    NOT_MATHCING_PASSWORD = '//p[normalize-space()="The two password fields didn\'t match."]'
    
    #ITEMS IN THE LIST
    CATAGORY_CONTENT = "//tbody[@id='category_content']//tr"
    CATAGORY_SEARCH = "//input[@id='part_category_search']"
    PRICE_BUTTON = "//p[normalize-space()='Price']"
    COPATIBILITY_BUTTON = "//input[@id='compatibility_enabled']"
    
    
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