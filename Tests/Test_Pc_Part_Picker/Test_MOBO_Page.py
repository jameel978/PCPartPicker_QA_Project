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
        self.website_page.go_to_product_page("Motherboards")

    def test_advanced_searching_in_MOBO_section(self):
        self.website_page.write_in_the_search_box("ATX")
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.apply_section_filter("ATX")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)

    def test_product_that_doesnt_exist(self):
        self.website_page.write_in_the_search_box("asdasdjsadasd")
        result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(result, "0 Compatible Products")

    def test_empty_search(self):
        old_result = self.website_page.get_number_of_product_in_the_page()
        self.website_page.write_in_the_search_box("  ")
        new_result = self.website_page.get_number_of_product_in_the_page()
        self.assertEqual(old_result, new_result)