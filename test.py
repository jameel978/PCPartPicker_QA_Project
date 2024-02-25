import unittest
from logic.website import PC_PART_PICKER
import time


class PCPARTPICKERTests(unittest.TestCase):
    def test_login(self):
        self.website_page = PC_PART_PICKER()
        self.website_page.login_flow('jameel978','Geme1533')
        time.sleep(100)

