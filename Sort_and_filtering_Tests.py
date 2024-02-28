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
        options.add_argument("--start-maximized")
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
        self.website_page.go_to_product_page("CPUs")
        self.website_page.write_in_the_search_box("7800X3D")
        result = self.website_page.get_title_of_the_first_product_in_the_page()
        self.assertIn("7800X3D", result)

    def test_empty_search(self):
        self.website_page.go_to_product_page("CPUs")
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.write_in_the_search_box("  ")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_product_that_doesnt_exist(self):
        self.website_page.go_to_product_page("CPUs")
        self.website_page.write_in_the_search_box("asdasdjsadasd")
        result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(result, "0 Compatible Products")

    def advanced_searching_in_CPU_section(self):
        self.website_page.go_to_product_page("CPUs")
        self.website_page.write_in_the_search_box("AM5")
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.apply_section_filter("AM5")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_advanced_searching_in_MOBO_section(self):
        self.website_page.go_to_product_page("Motherboards")
        self.website_page.write_in_the_search_box("ATX")
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.apply_section_filter("ATX")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_sorting_by_price_descending_order(self):
        self.website_page.go_to_product_page("CPUs")
        self.website_page.filter_by("Price",order = "descending")
        result = self.website_page.check_if_page_filtered_by_price("descending")
        self.assertTrue(result)

    def test_sorting_by_price_increasing_order(self):
        self.website_page.go_to_product_page("CPUs")
        self.website_page.filter_by("Price",order = "increasing")
        result = self.website_page.check_if_page_filtered_by_price("increasing")
        self.assertTrue(result)

    def test_price_range_slider_in_prodcut_page(self):
        self.website_page.go_to_product_page("CPUs")
        self.website_page.set_price_range_in_prodcut_page(100,350)
        self.website_page.filter_by("Price", order="increasing")
        increasing_result = self.website_page.check_if_prices_are_in_range(100,350)
        self.website_page.filter_by("Price", order="decreasing")
        decreasing_result = self.website_page.check_if_prices_are_in_range(100,350)
        self.assertTrue(increasing_result and decreasing_result)
