import unittest

from infra.Browser_wrapper import BrowserWrapper
from logic.PcPartPicker import Pc_Part_Picker
import concurrent.futures
from logic.helper_functions import *
from infra.Browser_wrapper import *
import time

class login_and_registration_tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(login_and_registration_tests, self).__init__(*args, **kwargs)
        config_location = "Configs/login_registration_tests.json"
        variables = get_test_variables(config_location)
        self.correct_username = variables['correct_username']
        self.correct_email = variables['correct_email']
        self.incorrect_username = variables['incorrect_username']
        self.invalid_username = variables['invalid_username']
        self.correct_password = variables['correct_password']
        self.incorrect_password = variables['incorrect_password']
        self.wrong_password = self.correct_password + 'a'
        self.invalid_password = 'A '
        self.rand_username = generate_random_username()
        self.rand_email = self.rand_username + "@gmail.com"
        self.rand_invalid_email = "   !$" + self.rand_email
        self.wrong_email = 'aa' + self.rand_email
        browser_caps = BrowserWrapper(config_location).get_caps()
        test_lists = [self.login_with_correct_credentials,self.login_with_wrong_password,self.login_with_wrong_Username,self.successful_registration,self.registration_with_already_registered_username,self.registration_with_invalid_username,self.registration_with_already_registered_email,self.registration_with_invalid_email,self.registration_with_not_matching_email,self.registration_with_not_matching_password,self.registration_with_invalid_password,self.registration_with_not_checking_tos,self.registration_with_not_checking_ucoc]
        self.inputs_list = [(tmp_test, browser) for tmp_test in test_lists for browser in browser_caps]
        self.test_type = get_test_config(config_location)["test_type"]
        self.test_URL = get_test_config(config_location)["URL"]
    def test_runner(self):
        if self.test_type == "parallel":
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.inputs_list)) as executer:
                executer.map(self.init_tests, self.inputs_list)
        else:
            for current_test in self.inputs_list:
                try:
                    self.init_tests(current_test)
                    print(current_test[0].__name__, "Passed on browser", current_test[1][0])
                except:
                    print(current_test[0].__name__, "Failed on browser" , current_test[1][0])
    def init_tests(self, input):
        input[0](input[1])
    def start_setUp(self,CAP):
        website = Pc_Part_Picker(*CAP)
        website.go_to_url(self.test_URL)
        return website
    def login_with_correct_credentials(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.account_login_flow(self.correct_username, self.correct_password)
        result = current_page.check_if_user_is_logged_in()
        time.sleep(10)
        self.assertTrue(result)

    def login_with_wrong_password(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.account_login_flow(self.correct_username, self.incorrect_username)
        result = current_page.check_if_user_entred_wrong_credentials()
        self.assertTrue(result)

    def login_with_wrong_Username(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.account_login_flow(self.incorrect_username, self.correct_password)
        result = current_page.check_if_user_entred_wrong_credentials()
        self.assertTrue(result)

    def successful_registration(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username,self.correct_password,self.rand_email)
        result = current_page.check_if_registration_is_complete()
        self.assertTrue(result)

    def registration_with_already_registered_username(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.correct_username,self.correct_password,self.rand_email)
        result = current_page.check_for_already_registered_username_error()
        self.assertTrue(result)

    def registration_with_invalid_username(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.invalid_username,self.correct_password,self.rand_email)
        result = current_page.check_for_invalid_username()
        self.assertTrue(result)

    def registration_with_already_registered_email(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username,self.rand_username,self.correct_email)
        result = current_page.check_for_already_registered_email()
        self.assertTrue(result)

    def registration_with_invalid_email(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username, self.correct_password, self.rand_invalid_email)
        result = current_page.check_for_invalid_email()
        self.assertTrue(result)

    def registration_with_not_matching_email(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username, self.correct_password, self.rand_email, self.wrong_email )
        result = current_page.check_for_not_matching_email()
        self.assertTrue(result)

    def registration_with_not_matching_password(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username, self.correct_password,password_repeat=self.wrong_password , email = self.rand_email)
        result = current_page.check_for_not_matching_password()
        self.assertTrue(result)

    def registration_with_invalid_password(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username, self.invalid_password, email = self.rand_email)
        result = current_page.check_for_registration_error()
        self.assertTrue(result)

    def registration_with_not_checking_tos(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username,self.correct_password,self.rand_email,TOS=False)
        result = current_page.check_for_registration_error()
        self.assertTrue(result)

    def registration_with_not_checking_ucoc(self,CAP):
        current_page = self.start_setUp(CAP)
        current_page.register_account_flow(self.rand_username,self.correct_password,self.rand_email,UCOC=False)
        result = current_page.check_for_registration_error()
        self.assertTrue(result)