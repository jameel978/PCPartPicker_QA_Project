import unittest
import os
from Logic.Pc_Part_Picker.Building_Pc_Base_page import *
from Infra.Browser_wrapper import *
from Logic.Utils import *


class building_pc_tests(unittest.TestCase):
    def __init__(self, methodName='runTest', cap=None):
        super().__init__(methodName)
        if cap == None:
            cap = BrowserWrapper().get_default_browser_cap()
        self.cap = cap
    def setUp(self):
        self.current_page = building_pc_page(self.cap)
        self.current_page.choose_random_part("Choose A CPU")
        self.current_page.choose_random_part("Choose A CPU Cooler")
        self.current_page.choose_random_part("Choose A Motherboard")
        self.current_page.choose_random_part("Choose Memory")
        self.current_page.choose_random_part("Choose Storage")
        self.current_page.choose_random_part("Choose A Video Card")
        self.current_page.choose_random_part("Choose A Case")
        self.current_page.choose_random_part("Choose A Power Supply")

    def test_build_random_pc(self):
        result = self.current_page.check_for_compatibility()
        self.assertTrue(result)

    def test_pc_build_permalink(self):
        actual_result = self.current_page.gell_build_parts()
        perma_link = self.current_page.get_build_perma_link()
        self.current_page.close_page()
        new_page = building_pc_page(self.cap)
        new_page.go_to_url(perma_link)
        restored_result = new_page.gell_build_parts()
        self.assertEqual(actual_result,restored_result)


    def tearDown(self):
        self.current_page.quit()
