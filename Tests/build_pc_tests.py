import unittest
from Logic.Building_Pc_Base_page import *
from Infra.Browser_wrapper import *
from Logic.Utils import *
import concurrent.futures


class building_pc_tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(building_pc_tests, self).__init__(*args, **kwargs)
        self.config_location = "../Configs/build_pc_tests.json"
    def test_runner(self):
        test_list = get_all_tests(self)
        browser_caps = BrowserWrapper(self.config_location).get_caps()
        inputs_list = [(tmp_test, browser) for tmp_test in test_list for browser in browser_caps]
        test_type = get_test_config(self.config_location)["test_type"]
        if test_type == "parallel":
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
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

    def test_compatibility_function(self,cap = None):
        current_page = building_pc_page(cap)
        current_page.choose_part_page_in_building_section("Choose A CPU")
        current_page.write_in_the_search_box("intel")
        current_page.choose_first_part()
        current_page.choose_part_page_in_building_section("Choose A Motherboard")
        current_page.turn_off_compatible_filter()
        current_page.write_in_the_search_box("AM5")
        current_page.choose_first_part()
        result = current_page.check_for_compatibility()
        self.assertFalse(result)

    def test_build_random_pc(self,cap = None):
        current_page = building_pc_page(cap)
        current_page.choose_random_part("Choose A CPU")
        current_page.choose_random_part("Choose A CPU Cooler")
        current_page.choose_random_part("Choose A Motherboard")
        current_page.choose_random_part("Choose Memory")
        current_page.choose_random_part("Choose Storage")
        current_page.choose_random_part("Choose A Video Card")
        current_page.choose_random_part("Choose A Case")
        current_page.choose_random_part("Choose A Power Supply")
        result = current_page.check_for_compatibility()
        self.assertTrue(result)

    def test_pc_build_permalink(self,cap = None):
        current_page = building_pc_page(cap)
        current_page.choose_random_part("Choose A CPU")
        current_page.choose_random_part("Choose A CPU Cooler")
        current_page.choose_random_part("Choose A Motherboard")
        current_page.choose_random_part("Choose Memory")
        current_page.choose_random_part("Choose Storage")
        current_page.choose_random_part("Choose A Video Card")
        current_page.choose_random_part("Choose A Case")
        current_page.choose_random_part("Choose A Power Supply")
        actual_result = current_page.gell_build_parts()
        perma_link = current_page.get_build_perma_link()
        current_page.close_page()
        new_page = building_pc_page(cap)
        new_page.go_to_url(perma_link)
        restored_result = new_page.gell_build_parts()
        self.assertEqual(actual_result,restored_result)



