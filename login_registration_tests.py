import unittest
from logic.PcPartPicker import Pc_Part_Picker
from selenium import webdriver
from logic.helper_functions import *
import time


class PCPARTPICKERTests(unittest.TestCase):

#cipevic841@gexige.com
#Beyond_dev
#A123456a

    def setUp(self):
        self.rand_username = generate_random_username()
        self.rand_email = self.rand_username + "@gmail.com"
        self.driver = webdriver.Chrome()
        self.driver.get("https://pcpartpicker.com/")
        self.website_page = Pc_Part_Picker(self.driver)

    def test_login_with_correct_credentials(self):
        self.website_page.account_login_flow('Beyond_dev', 'A123456a')
        result = self.website_page.check_if_user_is_logged_in()
        self.assertTrue(result)

    def test_login_with_wrong_password(self):
        self.website_page.account_login_flow('Beyond_dev', 'A123456aa')
        result = self.website_page.check_if_user_entred_wrong_credentials()
        self.assertTrue(result)

    def test_login_with_wrong_Username(self):
        self.website_page.account_login_flow('Beyond_deva', 'A123456a')
        result = self.website_page.check_if_user_entred_wrong_credentials()
        self.assertTrue(result)

    def test_successful_registration(self):
        self.website_page.register_account_flow(self.rand_username,'A123456a',self.rand_email)
        result = self.website_page.check_if_registration_is_complete()
        self.assertTrue(result)

    def test_registration_with_already_registered_username(self):
        self.website_page.register_account_flow('Beyond_dev','A123456a',self.rand_email)
        result = self.website_page.check_for_already_registered_username_error()
        self.assertTrue(result)

    def test_registration_with_invalid_username(self):
        self.website_page.register_account_flow('Beyond_dev12311  123!$%','A123456a',self.rand_email)
        result = self.website_page.check_for_invalid_username()
        self.assertTrue(result)

    def test_registration_with_already_registered_email(self):
        self.website_page.register_account_flow(self.rand_username,self.rand_username,"cipevic841@gexige.com")
        result = self.website_page.check_for_already_registered_email()
        self.assertTrue(result)

    def test_registration_with_invalid_email(self):
        self.website_page.register_account_flow(self.rand_username, 'A123456a', "   !$" + self.rand_email,)
        result = self.website_page.check_for_invalid_email()
        self.assertTrue(result)

    def test_registration_with_not_matching_email(self):
        self.website_page.register_account_flow(self.rand_username, 'A123456a', self.rand_email,email_repeat="aa" + self.rand_email)
        result = self.website_page.check_for_not_matching_email()
        self.assertTrue(result)

    def test_registration_with_not_matching_password(self):
        self.website_page.register_account_flow(self.rand_username, 'A123456a',password_repeat="A12345226a", email = self.rand_email)
        result = self.website_page.check_for_not_matching_password()
        self.assertTrue(result)

    def test_registration_with_invalid_password(self):
        self.website_page.register_account_flow(self.rand_username, 'A ', email = self.rand_email)
        result = self.website_page.check_for_registration_error()
        self.assertTrue(result)

    def test_registration_with_not_checking_tos(self):
        self.website_page.register_account_flow(self.rand_username,'A123456a',self.rand_email,TOS=False)
        result = self.website_page.check_for_registration_error()
        self.assertTrue(result)

    def test_registration_with_not_checking_ucoc(self):
        self.website_page.register_account_flow(self.rand_username,'A123456a',self.rand_email,UCOC=False)
        result = self.website_page.check_for_registration_error()
        self.assertTrue(result)