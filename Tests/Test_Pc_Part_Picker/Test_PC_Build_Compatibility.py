import unittest
from Logic.Pc_Part_Picker.Building_Pc_Base_page import *
from Infra.Browser_wrapper import *

class building_pc_tests(unittest.TestCase):
    def __init__(self, methodName='runTest', cap=None):
        super().__init__(methodName)
        if cap == None:
            cap = BrowserWrapper().get_default_browser_cap()
        self.cap = cap

    def setUp(self):
        self.current_page = building_pc_page(self.cap)

    def test_compatibility_function(self):
        self.current_page.choose_part_page_in_building_section("Choose A CPU")
        self.current_page.write_in_the_search_box("intel")
        self.current_page.choose_first_part()
        self.current_page.choose_part_page_in_building_section("Choose A Motherboard")
        self.current_page.turn_off_compatible_filter()
        self.current_page.write_in_the_search_box("AM5")
        self.current_page.choose_first_part()
        result = self.current_page.check_for_compatibility()
        self.assertFalse(result)

    def tearDown(self):
        self.current_page.quit()
