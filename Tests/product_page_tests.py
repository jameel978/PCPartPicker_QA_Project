import unittest
from Logic.Product_Base_Page import *
from Infra.Browser_wrapper import BrowserWrapper
import concurrent.futures
from Logic.Utils import *
import time

class product_page_tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(product_page_tests, self).__init__(*args, **kwargs)
        self.config_location = "../Configs/Product_page_tests.json"

    def test_runner(self):
        test_list = get_all_tests(self)
        browser_caps = BrowserWrapper(self.config_location).get_caps()
        inputs_list = [(tmp_test, browser) for tmp_test in test_list for browser in browser_caps]
        test_type = get_test_config(self.config_location)["test_type"]
        if test_type == "parallel":
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                executor.map(self.init_tests, inputs_list)
        else:
            for current_test in inputs_list:
                self.init_tests(current_test)

    def init_tests(self, input_):
        try:
            input_[0](input_[1])
            print(input_[0].__name__, "Passed on browser", input_[1][0])
        except:
            print(input_[0].__name__, "Failed on browser", input_[1][0])

    def test_searching_in_cpu_section(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("CPUs")
        website_page.write_in_the_search_box("7800X3D")
        result = website_page.get_title_of_the_first_product_in_the_page()
        self.assertIn("7800X3D", result)

    def test_empty_search(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("CPUs")
        old_result = website_page.get_number_of_product_in_the_page()
        website_page.write_in_the_search_box("  ")
        new_result = website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_product_that_doesnt_exist(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("CPUs")
        website_page.write_in_the_search_box("asdasdjsadasd")
        result = website_page.get_number_of_product_in_the_page()
        self.assertEqual(result, "0 Compatible Products")

    def test_advanced_searching_in_CPU_section(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("CPUs")
        website_page.write_in_the_search_box("AM5")
        old_result = website_page.get_number_of_product_in_the_page()
        website_page.apply_section_filter("AM5")
        new_result = website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_advanced_searching_in_MOBO_section(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("Motherboards")
        website_page.write_in_the_search_box("ATX")
        old_result = website_page.get_number_of_product_in_the_page()
        website_page.apply_section_filter("ATX")
        new_result = website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_sorting_by_price_descending_order(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("CPUs")
        website_page.filter_by("Price",order = "descending")
        result = website_page.check_if_page_filtered_by_price("descending")
        self.assertTrue(result)

    def test_sorting_by_price_increasing_order(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("CPUs")
        website_page.filter_by("Price",order = "increasing")
        result = website_page.check_if_page_filtered_by_price("increasing")
        self.assertTrue(result)

    def test_price_range_slider_in_product_page(self,cap= None):
        website_page = Product_page(cap)
        website_page.go_to_product_page("CPUs")
        website_page.set_price_range_in_prodcut_page(100,332)
        website_page.filter_by("Price", order="increasing")
        increasing_result = website_page.check_if_prices_are_in_range(100,332)
        website_page.filter_by("Price", order="decreasing")
        decreasing_result = website_page.check_if_prices_are_in_range(100,332)
        self.assertTrue(increasing_result and decreasing_result)


