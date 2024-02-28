from selenium.webdriver.common.by import By
from infra.Driverinstance import Driver_instance
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from logic.helper_functions import *


class Pc_Part_Picker(Driver_instance):
    # HOMEPAGE
    # https://pcpartpicker.com/
    LOGIN_BUTTON = "//ul[@class='nav__account nav__account--desktop list-unstyled']/li[@class='nav__account--login']"
    REGISTER_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--register']//a[normalize-space()='Register']"
    START_BUILDING_YOUR_PC_BUTTON = "//a[normalize-space()='Start Your Build']"
    BUILDER_BUTTON = "//ul[@role='presentation']//li[@class='nav__categories--partlist']"
    PRODUCT_BUTTON = "//a[contains(text(),'Products')]"
    GUIDES_BUTTON = "//ul[@role='presentation']//li[@class='nav__categories--guides']"
    COMPLETE_BUILDS_BUTTON = "//a[contains(text(),'Completed Builds')]"
    TRENDS_BUTTON = "//a[contains(text(),'Trends')]"
    FOURMS_BUTTON = "//a[contains(text(),'Forums')]"

    # AFTER LOGIN_BUTTON
    LOGOUT_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--logout']//a[normalize-space()='Log Out']"
    SAVED_PARTS_BUTTON = "//ul[@role='presentation']//a[contains(text(),'Saved Parts Lists')]"
    FAVORITE_PART_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--favorites']//a[contains(text(),'Favorite Parts')]"

    # BUILDPCSECTION
    # https://pcpartpicker.com/list/
    CHOOSE_PART = "//a[normalize-space()='"
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

    # PRODUCT_PAGE
    # https://pcpartpicker.com/products/
    SECTION_PAGE = "//ul[@class='inside']//a[normalize-space()='"
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

    NUMBER_OF_FOUND_PARTS = "//h2[contains(text(),'Compatible Product')]"

    # LOGIN_PAGE
    USER_INPUT = "//input[@id='id_username']"
    PASSWORD_INPUT = "//input[@id='id_password']"
    SUBMIT_BUTTON = "//input[@id='input_recaptcha']"
    WRONG_CREDENTAILS = "//p[normalize-space()='Invalid username or password. Please try again.']"

    # REGISTRATION_PAGE
    EMAIL_INPUT = "//input[@id='id_email']"
    EMAIL_INPUT_SECOND = "//input[@id='id_email2']"
    FIRST_PASSWORD_INPUT_REGISTRATION = "//input[@id='id_password1']"
    SECOND_PASSWORD_INPUT_REGISTRATION = "//input[@id='id_password2']"
    ACCEPT_TOS_CHECKBOX = "//label[@for='id_accept_tos']"
    ACCEPT_UCOC_CHECKBOX = "//label[@for='id_accept_ucoc']"
    COMPLETE_REGISTRATION = "//input[@id='input_recaptcha']"
    REGISTRATION_IS_COMPLETED = "//h1[normalize-space()='Registration Complete']"

    GEBERAL_TEXT_ERROR = "//p[@class='text-error']"
    ALREADY_REGISTERED_USERNAME = "//p[normalize-space()='A user with that username already exists.']"
    IVALID_USERNAME = "//p[contains(text(),'This value may contain only letters, numbers and @')]"
    ALREADY_REGISTERED_EMAIL = "//p[contains(text(),'This email address is already in use. Please suppl')]"
    INVALID_EMAIL_ERROR = "//p[@class='text-error'][normalize-space()='Enter a valid email address.']"
    NOT_MATHCING_EMAIL = '(//p[normalize-space()="The two email fields didn\'t match."])'
    NOT_MATHCING_PASSWORD = '//p[normalize-space()="The two password fields didn\'t match."]'

    # ITEMS IN THE LIST
    CATAGORY_CONTENT = "//tbody[@id='category_content']//tr"
    CATAGORY_CONTENT_NAMES = "//tbody[@id='category_content']//tr//td[@class='td__name']"
    CATAGORY_CONTENT_COUNT = "//h2[@class='pp-filter-count']"
    CATAGORY_SEARCH = "//input[@id='part_category_search']"
    PRICE_ELEMNT = ".//td[@class='td__price']"
    COPATIBILITY_BUTTON = "//input[@id='compatibility_enabled']"
    FILTER_BY_BUTTON = "//p[normalize-space()='"
    PRICE_SLIDER = "//div[@id='filter_slide_X']//div[@class='obj-filter-dualslide ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']"
    PRICE_SLIDER_MAX_RANGE = "//div[@class='obj-filter-slide-right ui-slider-horizontal-labelbox-label']"
    PRICE_SLIDER_MIN_RANGE = "//div[@class='obj-filter-slide-left ui-slider-horizontal-labelbox-label']"
    SLIDER_LEFT_HANDLE = "//div[@id='filter_slide_X']//span[1]"
    SLIDER_RIGHT_HANDLE = ".//span[@tabindex='0'][2]"
    LEFT_RIGHT_SLIDERS = "//div[@id='filter_slide_X']//div[@class='obj-filter-dualslide ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']//span"
    #CPU SECTION
    CPU_COCKET = "//h3[normalize-space()='Socket']"
    FILTER_SECTION = "//label[normalize-space()='"
    EXPAND_ALL_ELEMENTS = "//ul//span[@class='arrow__small arrow__small--down']//*[name()='svg']"

    def __init__(self, driver):
        super().__init__(driver)

    def account_login_flow(self, username, password):
        self.Find_and_click_on_element(self.LOGIN_BUTTON)
        self.Find_and_send_input_to_element(self.USER_INPUT, username)
        self.Find_and_send_input_to_element(self.PASSWORD_INPUT, password)
        self.Find_and_click_on_element(self.SUBMIT_BUTTON)

    def register_account_flow(self, username, password, email, email_repeat=True, password_repeat=True, TOS=True,
                              UCOC=True):
        if isinstance(email_repeat, bool):
            email_repeat = email
        if isinstance(password_repeat, bool):
            password_repeat = password
        self.Find_and_click_on_element(self.REGISTER_BUTTON)
        self.Find_and_send_input_to_element(self.USER_INPUT, username)
        self.Find_and_send_input_to_element(self.EMAIL_INPUT, email)
        self.Find_and_send_input_to_element(self.EMAIL_INPUT_SECOND, email_repeat)
        self.Find_and_send_input_to_element(self.FIRST_PASSWORD_INPUT_REGISTRATION, password)
        self.Find_and_send_input_to_element(self.SECOND_PASSWORD_INPUT_REGISTRATION, password_repeat)
        if TOS:
            self.Find_and_click_on_element(self.ACCEPT_TOS_CHECKBOX)
        if UCOC:
            self.Find_and_click_on_element(self.ACCEPT_UCOC_CHECKBOX)
        self.Find_and_click_on_element(self.COMPLETE_REGISTRATION)

    def check_for_registration_error(self):
        return self.is_element_found(self.GEBERAL_TEXT_ERROR, sec=3)

    def check_for_already_registered_username_error(self):
        return self.is_element_found(self.ALREADY_REGISTERED_USERNAME, sec=3)

    def check_for_invalid_username(self):
        return self.is_element_found(self.IVALID_USERNAME, sec=3)

    def check_for_invalid_email(self):
        return self.is_element_found(self.INVALID_EMAIL_ERROR, sec=3)

    def check_for_already_registered_email(self):
        return self.is_element_found(self.ALREADY_REGISTERED_EMAIL, sec=3)

    def check_for_not_matching_email(self):
        return self.is_element_found(self.NOT_MATHCING_EMAIL, sec=3)

    def check_for_not_matching_password(self):
        return self.is_element_found(self.NOT_MATHCING_PASSWORD, sec=3)

    def check_if_registration_is_complete(self):
        return self.is_element_found(self.REGISTRATION_IS_COMPLETED, sec=3)

    def check_if_user_is_logged_in(self):
        return self.is_element_found(self.LOGOUT_BUTTON, sec=3)

    def check_if_user_entred_wrong_credentials(self):
        return self.is_element_found(self.WRONG_CREDENTAILS, sec=3)

    def go_to_product_page(self,section):
        Section = self.SECTION_PAGE + section + "']"
        self.Find_and_click_on_element(Section)

    def write_in_the_search_box(self, txt):
        self.Find_and_send_input_to_element(self.CATAGORY_SEARCH, txt)
        time.sleep(3)

    def get_title_of_the_first_product_in_the_page(self):
        return self.wait_and_get_element_by_xpath(self.CATAGORY_CONTENT_NAMES).text

    def get_number_of_product_in_the_page(self):
        ans = "Loading Products"
        #To wait for the page products in the page to load
        while ans == "Loading Products":
            ans = self.wait_and_get_element_by_xpath(self.CATAGORY_CONTENT_COUNT).text
            time.sleep(0.25)
        return ans

    def apply_section_filter(self,section_filter):
        #self.expand_all_sections()
        cur_elem = self.FILTER_SECTION + section_filter + "']//preceding-sibling::input"
        self.Find_and_click_on_element(cur_elem,click_using_javescript = True)
        time.sleep(3)

    def expand_all_sections(self):
        all_expand_buttons = self.wait_and_get_elements_by_xpath(self.EXPAND_ALL_ELEMENTS)
        for elem in all_expand_buttons:
            if elem.is_displayed() and elem.is_enabled():
                self.click_on_elem(elem)


    def filter_by(self,fltr,order):
        Section = self.FILTER_BY_BUTTON + fltr + "']"
        if order == "descending":
            self.Find_and_click_on_element(Section)
            self.Find_and_click_on_element(Section)
        elif order == "increasing":
            self.Find_and_click_on_element(Section)

    def check_if_page_filtered_by_price(self,order):
        prices = []
        all_page_elements = self.wait_and_get_elements_by_xpath(self.CATAGORY_CONTENT)
        for elem in all_page_elements:
            #[1:-3] to remove # sign and add word
            tmp_price = elem.find_element(By.XPATH,self.PRICE_ELEMNT).text[1:-3]
            prices.append(float(tmp_price))
        return check_if_list_is_in_order(prices,order)

    def set_price_range_in_prodcut_page(self,start_price,end_price):
        current_max_price = self.wait_and_get_element_by_xpath(self.PRICE_SLIDER_MAX_RANGE)
        current_min_price = self.wait_and_get_element_by_xpath(self.PRICE_SLIDER_MIN_RANGE)
        slider_elements = self.wait_and_get_elements_by_xpath(self.LEFT_RIGHT_SLIDERS)
        start_element = slider_elements[0]
        end_element = slider_elements[1]
        self.drag_slider_elements(start_element,current_min_price,start_price)
        #self.drag_slider_elements(end_element, current_max_price,end_price)
        time.sleep(3)