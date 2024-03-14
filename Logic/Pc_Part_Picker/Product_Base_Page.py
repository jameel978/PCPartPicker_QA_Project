from Infra.Driver_instance import Driverinstance
from selenium.webdriver.common.by import By
import time
from Logic.Utils import *


class Product_page(Driverinstance):

    # PRODUCT_PAGE
    # https://pcpartpicker.com/products/
    SECTION_PAGE = "//ul[@class='inside']//a[normalize-space()='"
    NUMBER_OF_FOUND_PARTS = "//h2[contains(text(),'Compatible Product')]"

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

    #CPU SECTION
    CPU_COCKET = "//h3[normalize-space()='Socket']"
    FILTER_SECTION = "//label[normalize-space()='"
    EXPAND_ALL_ELEMENTS = "//ul//span[@class='arrow__small arrow__small--down']//*[name()='svg']"
    PAGE_URL = "https://pcpartpicker.com/products"

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.PAGE_URL)
        time.sleep(3)
        time.sleep(3)
        if self.get_page_title() == "Just a moment...":
            self.quit()
            raise Exception("Test Failed, Captcha Detected")
        #self.refresh_driver()
        #time.sleep(3)
        #self.print_html_page()

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

    def filter_by(self,fltr,order):
        Section = self.FILTER_BY_BUTTON + fltr + "']"
        #print(Section)
        if order == "descending":
            self.Find_and_click_on_element(Section)
            time.sleep(2)
            self.Find_and_click_on_element(Section)
        elif order == "increasing":
            self.Find_and_click_on_element(Section)
        time.sleep(3)

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

