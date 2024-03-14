import time
import unittest
from Logic.Pc_Part_Picker.Login_Registration_Base_Page import *
from Infra.Browser_wrapper import *
from Logic.Utils import *
import os

class login_registration_tests(unittest.TestCase):
    def __init__(self, methodName='runTest', cap=None):
        super().__init__(methodName)
        if cap == None:
            cap = BrowserWrapper().get_default_browser_cap()
        self.cap = cap
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self.variables = read_json(os.path.join(cur_dir, "Configs", "Tests_config.json"))['login_registration_tests_vars']
        self.rand_email = generate_random_username() + "@gmail.com"
        self.rand_invalid_email = "   !$" + self.rand_email
        self.wrong_email = 'aa' + self.rand_email

    def setUp(self):
        self.current_page = Login_Registration_Page(self.cap)

    def test_login_with_correct_credentials(self):
        self.current_page.account_login_flow(self.variables['correct_username'], self.variables['correct_password'])
        result = self.current_page.check_if_user_is_logged_in()
        self.assertTrue(result)
        self.current_page.close_page()

    def test_login_with_wrong_password(self):
        self.current_page.account_login_flow(self.variables['correct_username'], self.variables['incorrect_username'])
        result = self.current_page.check_if_user_entred_wrong_credentials()
        self.assertTrue(result)

    def test_login_with_wrong_Username(self):
        self.current_page.account_login_flow(self.variables['incorrect_username'], self.variables['correct_password'])
        result = self.current_page.check_if_user_entred_wrong_credentials()
        self.assertTrue(result)

    def test_successful_registration(self):
        self.current_page.register_account_flow(generate_random_username(),self.variables['correct_password'],self.rand_email)
        result = self.current_page.check_if_registration_is_complete()
        self.assertTrue(result)

    def test_registration_with_already_registered_username(self):
        self.current_page.register_account_flow(self.variables['correct_username'],self.variables['correct_password'],self.rand_email)
        result = self.current_page.check_for_already_registered_username_error()
        self.assertTrue(result)

    def test_registration_with_invalid_username(self):
        self.current_page.register_account_flow(self.variables['invalid_username'],self.variables['correct_password'],self.rand_email)
        result = self.current_page.check_for_invalid_username()
        self.assertTrue(result)
  
    def test_registration_with_already_registered_email(self):
        self.current_page.register_account_flow(generate_random_username(),generate_random_password(),self.variables['correct_email'])
        result = self.current_page.check_for_already_registered_email()
        self.assertTrue(result)

    def test_registration_with_invalid_email(self):
        self.current_page.register_account_flow(generate_random_username(), self.variables['correct_password'], self.rand_invalid_email)
        result = self.current_page.check_for_invalid_email()
        self.assertTrue(result)

    def test_registration_with_not_matching_email(self):
        self.current_page.register_account_flow(generate_random_username(), self.variables['correct_password'], self.rand_email, self.wrong_email )
        result = self.current_page.check_for_not_matching_email()
        self.assertTrue(result)

    def test_registration_with_not_matching_password(self):
        self.current_page.register_account_flow(generate_random_username(), self.variables['correct_password'],password_repeat=self.variables['correct_password'] + 'a' , email = self.rand_email)
        result = self.current_page.check_for_not_matching_password()
        self.assertTrue(result)

    def test_registration_with_invalid_password(self):
        self.current_page.register_account_flow(generate_random_username(), self.variables["invalid_password"], email = self.rand_email)
        result = self.current_page.check_for_registration_error()
        self.assertTrue(result)

    def test_registration_with_not_checking_tos(self):
        self.current_page.register_account_flow(generate_random_username(),self.variables['correct_password'],self.rand_email,TOS=False)
        result = self.current_page.check_for_registration_error()
        self.assertTrue(result)

    def test_registration_with_not_checking_ucoc(self):
        self.current_page.register_account_flow(generate_random_username(),self.variables['correct_password'],self.rand_email,UCOC=False)
        result = self.current_page.check_for_registration_error()
        self.assertTrue(result)

    def tearDown(self):
        self.current_page.quit()
