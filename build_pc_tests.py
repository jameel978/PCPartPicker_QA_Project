import unittest
from logic.PcPartPicker import Pc_Part_Picker
from selenium import webdriver
from logic.helper_functions import *
import time


class building_pc_tests(unittest.TestCase):
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
        self.driver.get("https://pcpartpicker.com/list/")
        self.website_page = Pc_Part_Picker(",","","",driver = self.driver)

    def test_compatibility_function(self):
        self.website_page.choose_part_page_in_building_section("Choose A CPU")
        self.website_page.write_in_the_search_box("intel")
        self.website_page.choose_first_part()
        self.website_page.choose_part_page_in_building_section("Choose A Motherboard")
        self.website_page.turn_off_compatible_filter()
        self.website_page.write_in_the_search_box("AM5")
        self.website_page.choose_first_part()
        result = self.website_page.check_for_compatibility()
        self.assertFalse(result)
    def test_build_random_pc(self):
        self.website_page.choose_random_part("Choose A CPU")
        self.website_page.choose_random_part("Choose A CPU Cooler")
        self.website_page.choose_random_part("Choose A Motherboard")
        self.website_page.choose_random_part("Choose Memory")
        self.website_page.choose_random_part("Choose Storage")
        self.website_page.choose_random_part("Choose A Video Card")
        self.website_page.choose_random_part("Choose A Case")
        self.website_page.choose_random_part("Choose A Power Supply")
        result = self.website_page.check_for_compatibility()
        self.assertTrue(result)

    def test_pc_build_permalink(self):
        self.website_page.choose_random_part("Choose A CPU")
        self.website_page.choose_random_part("Choose A CPU Cooler")
        self.website_page.choose_random_part("Choose A Motherboard")
        self.website_page.choose_random_part("Choose Memory")
        self.website_page.choose_random_part("Choose Storage")
        self.website_page.choose_random_part("Choose A Video Card")
        self.website_page.choose_random_part("Choose A Case")
        self.website_page.choose_random_part("Choose A Power Supply")
        actual_result = self.website_page.gell_build_parts()
        perma_link = self.website_page.get_build_perma_link()
        self.website_page.close_browser()
        self.setUp()
        self.website_page.go_to_url(perma_link)
        restored_result = self.website_page.gell_build_parts()
        self.assertEqual(actual_result,restored_result)



