import unittest
from Logic.Pc_Part_Picker.Product_Base_Page import *
from Infra.Browser_wrapper import BrowserWrapper

class product_page_tests(unittest.TestCase):
    def __init__(self, methodName='runTest', cap=None):
        super().__init__(methodName)
        if cap == None:
            cap = BrowserWrapper().get_default_browser_cap()
        self.cap = cap

    def setUp(self):
        self.website_page = Product_page(self.cap)
        self.website_page.go_to_product_page("CPUs")

    def test_searching_in_cpu_section(self):
        self.website_page.write_in_the_search_box("7800X3D")
        result = self.website_page.get_title_of_the_first_product_in_the_page()
        self.assertIn("7800X3D", result)

    def test_empty_search(self):
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.write_in_the_search_box("  ")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)


    def test_advanced_searching_in_CPU_section(self):
        self.website_page.write_in_the_search_box("AM5")
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.apply_section_filter("AM5")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)


    def test_sorting_by_price_descending_order(self):
        self.website_page.filter_by("Price", order="descending")
        result = self.website_page.check_if_page_filtered_by_price("descending")
        self.assertTrue(result)

    def test_sorting_by_price_increasing_order(self):
        self.website_page.filter_by("Price", order="increasing")
        result = self.website_page.check_if_page_filtered_by_price("increasing")
        self.assertTrue(result)

    def test_price_range_slider_in_product_page(self):
        self.website_page.set_price_range_in_prodcut_page(100, 332)
        self.website_page.filter_by("Price", order="increasing")
        increasing_result = self.website_page.check_if_prices_are_in_range(100, 332)
        self.website_page.filter_by("Price", order="decreasing")
        decreasing_result = self.website_page.check_if_prices_are_in_range(100, 332)
        self.assertTrue(increasing_result and decreasing_result)

    def tearDown(self):
        self.website_page.quit()
