from Infra.Driver_instance import Driverinstance
from selenium.webdriver.common.by import By
import time
from Logic.Utils import *


class building_pc_page(Driverinstance):
    # HOMEPAGE
    # https://pcpartpicker.com/


    NUMBER_OF_FOUND_PARTS = "//h2[contains(text(),'Compatible Product')]"

    # LOGIN_PAGE


    # ITEMS IN THE LIST
    CATAGORY_CONTENT = "//tbody[@id='category_content']//tr"
    CATAGORY_CONTENT_NAMES = "//tbody[@id='category_content']//tr//td[@class='td__name']"
    CATAGORY_CONTENT_COUNT = "//h2[@class='pp-filter-count']"
    CATAGORY_SEARCH = "//input[@id='part_category_search']"
    PRICE_ELEMNT = ".//td[@class='td__price']"
    ADD_PART = "//tr//button[@class='td__add button button--small pp_add_part'][normalize-space()='Add']"
    COPATIBILITY_BUTTON = "//input[@id='compatibility_enabled']"
    FILTER_BY_BUTTON = "//p[normalize-space()='"
    PRICE_SLIDER = "//div[@id='filter_slide_X']//div[@class='obj-filter-dualslide ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']"
    PRICE_SLIDER_MAX_RANGE = "//div[@class='obj-filter-slide-right ui-slider-horizontal-labelbox-label']"
    PRICE_SLIDER_MIN_RANGE = "//div[@class='obj-filter-slide-left ui-slider-horizontal-labelbox-label']"
    SLIDER_LEFT_HANDLE = "//div[@id='filter_slide_X']//span[1]"
    SLIDER_RIGHT_HANDLE = ".//span[@tabindex='0'][2]"
    LEFT_RIGHT_SLIDERS = "//div[@id='filter_slide_X']//div[@class='obj-filter-dualslide ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']//span"
    SECTION_PAGE = "//ul[@class='inside']//a[normalize-space()='"

    #CPU SECTION
    CPU_COCKET = "//h3[normalize-space()='Socket']"
    FILTER_SECTION = "//label[normalize-space()='"
    EXPAND_ALL_ELEMENTS = "//ul//span[@class='arrow__small arrow__small--down']//*[name()='svg']"

    CHOOSE_PART = "//a[normalize-space()='"
    COMPATIBILITY_WARNING = "//p[@class='partlist__compatibility--warning']"
    PERMA_LINK = "//div[@class='actionBox-2023 actionBox__permalink']//input"
    BUILD_PARTS = "//a[@class='actionBox__markupLink actionBox__markup--text tooltip']"
    MARK_UP_TEXT = "//textarea[@id='markup_text']"
    PAGE_URL = "https://pcpartpicker.com/list/"

    SOCKET_TYPE = "//td[@class='td__spec td__spec--1']//h6[@class='specLabel']"
    MOBO_FORMFACTOR = "//h6[@class='specLabel'][normalize-space()='Form Factor']"
    RAM_TYPE = "//h6[@class='specLabel'][normalize-space()='Speed']"
    GPU_LENGTH = "//h6[@class='specLabel'][normalize-space()='Length']"

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.PAGE_URL)
        time.sleep(3)
        time.sleep(3)
        if self.get_page_title() == "Just a moment...":
            raise Exception("Test Failed, Captcha Detected")
        #self.refresh_driver()
        #time.sleep(3)
        #self.print_html_page()




    def filter_by(self,fltr,order):
        Section = self.FILTER_BY_BUTTON + fltr + "']"
        if order == "descending":
            self.Find_and_click_on_element(Section)
            self.Find_and_click_on_element(Section)
        elif order == "increasing":
            self.Find_and_click_on_element(Section)
        time.sleep(2)

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
       # print(self.get_element_by_xpath(self.PRICE_SLIDER).size['width'])
        start_element = slider_elements[0]
        end_element = slider_elements[1]
        self.drag_slider_elements(start_element,current_min_price,start_price)
        self.drag_slider_elements(end_element, current_max_price,end_price)
        time.sleep(3)

    def check_if_prices_are_in_range(self,price_start,price_end):
        all_page_elements = self.wait_and_get_elements_by_xpath(self.CATAGORY_CONTENT)
        for elem in all_page_elements:
            #[1:-3] to remove # sign and add word
            tmp_price = elem.find_element(By.XPATH,self.PRICE_ELEMNT).text[1:-3]
            if (float(tmp_price) < price_start) and (float(tmp_price) > price_end):
                return False
        return True

    def turn_off_compatible_filter(self):
        elem = self.wait_and_get_element_by_xpath(self.COPATIBILITY_BUTTON)
        self.click_on_elem(elem)

    def choose_part_page_in_building_section(self,section):
        Section = self.CHOOSE_PART + section + "']"
        self.wait_and_get_element_by_xpath(Section,sec=5).click()

    def choose_random_part(self,section):
        Section = self.CHOOSE_PART + section + "']"
        self.click_on_elem(self.wait_and_get_element_by_xpath(Section,sec=5))
        all_page_elements = self.wait_and_get_elements_by_xpath(self.ADD_PART)
        button = random.choice(all_page_elements)
        time.sleep(1)
        self.click_on_elem(button)
        if section == "Choose A Motherboard":
            return button.find_element(By.XPATH,self.SOCKET_TYPE).text


    def choose_first_part(self):
        all_page_elements = self.wait_and_get_elements_by_xpath(self.ADD_PART)
        button = all_page_elements[0]
        self.click_on_elem(button)

    def check_for_compatibility(self):
        try:
            self.wait_and_get_element_by_xpath(self.COMPATIBILITY_WARNING,sec=5)
            return False
        except:
            return True

    def get_build_perma_link(self):
        perma_link = self.wait_and_get_element_by_xpath(self.PERMA_LINK)
        return perma_link.get_attribute("value")

    def gell_build_parts(self):
        self.wait_and_get_element_by_xpath(self.BUILD_PARTS).click()
        return self.wait_and_get_element_by_xpath(self.MARK_UP_TEXT).text


    def go_to_product_page(self,section):
        Section = self.SECTION_PAGE + section + "']"
        self.Find_and_click_on_element(Section)

    def write_in_the_search_box(self, txt):
        self.Find_and_send_input_to_element(self.CATAGORY_SEARCH, txt)
        time.sleep(3)