import unittest
from logic.PcPartPicker import Pc_Part_Picker
from selenium import webdriver
from logic.helper_functions import *
import time


class PCPARTPICKERTests(unittest.TestCase):

    # cipevic841@gexige.com
    # Beyond_dev
    # A123456a

    def setUp(self):
        # Create Chromeoptions instance
        options = webdriver.ChromeOptions()
        # Adding argument to disable the AutomationControlled flag
        options.add_argument("--disable-blink-features=AutomationControlled")
        # Exclude the collection of enable-automation switches
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Turn-off userAutomationExtension
        options.add_experimental_option("useAutomationExtension", False)
        # Setting the driver path and requesting a page
        self.driver = webdriver.Chrome(options=options)
        # Changing the property of the navigator value for webdriver to undefined
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        # self.driver = webdriver.Chrome()
        self.driver.get("https://pcpartpicker.com/products/")
        self.website_page = Pc_Part_Picker(self.driver)

    def searching_in_cpu_section(self):
        self.website_page.go_to_CPU_section()
        self.website_page.wrtie_in_the_search_box("7800X3D")
        result = self.website_page.get_title_of_the_first_product_in_the_page()
        self.assertIn("7800X3D", result)

    def test_empty_search(self):
        self.website_page.go_to_CPU_section()
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.wrtie_in_the_search_box("  ")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_advanced_searching_in_cpu_section(self):
        self.website_page.go_to_CPU_section()
        self.website_page.wrtie_in_the_search_box("AM5")
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.apply_section_filter("AM5")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)