import unittest
from Logic.Pc_Part_Picker.Login_Registration_Base_Page import *
from Infra.Browser_wrapper import *
from Logic.Utils import *
import concurrent.futures



class login_registration_tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(login_registration_tests, self).__init__(*args, **kwargs)
        self.config_location = "../Configs/login_registration_tests.json"
        self.variables = get_test_variables(self.config_location)
        self.rand_email = generate_random_username() + "@gmail.com"
        self.rand_invalid_email = "   !$" + self.rand_email
        self.wrong_email = 'aa' + self.rand_email

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

    def test_login_with_correct_credentials(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.account_login_flow(self.variables['correct_username'], self.variables['correct_password'])
        result = current_page.check_if_user_is_logged_in()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_login_with_wrong_password(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.account_login_flow(self.variables['correct_username'], self.variables['incorrect_username'])
        result = current_page.check_if_user_entred_wrong_credentials()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_login_with_wrong_Username(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.account_login_flow(self.variables['incorrect_username'], self.variables['correct_password'])
        result = current_page.check_if_user_entred_wrong_credentials()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()


    def test_successful_registration(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(),self.variables['correct_password'],self.rand_email)
        result = current_page.check_if_registration_is_complete()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_already_registered_username(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(self.variables['correct_username'],self.variables['correct_password'],self.rand_email)
        result = current_page.check_for_already_registered_username_error()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_invalid_username(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(self.variables['invalid_username'],self.variables['correct_password'],self.rand_email)
        result = current_page.check_for_invalid_username()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_already_registered_email(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(),generate_random_password(),self.variables['correct_email'])
        result = current_page.check_for_already_registered_email()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_invalid_email(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(), self.variables['correct_password'], self.rand_invalid_email)
        result = current_page.check_for_invalid_email()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_not_matching_email(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(), self.variables['correct_password'], self.rand_email, self.wrong_email )
        result = current_page.check_for_not_matching_email()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_not_matching_password(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(), self.variables['correct_password'],password_repeat=self.variables['correct_password'] + 'a' , email = self.rand_email)
        result = current_page.check_for_not_matching_password()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_invalid_password(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(), self.variables["invalid_password"], email = self.rand_email)
        result = current_page.check_for_registration_error()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_not_checking_tos(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(),self.variables['correct_password'],self.rand_email,TOS=False)
        result = current_page.check_for_registration_error()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()

    def test_registration_with_not_checking_ucoc(self,CAP = None):
        current_page = Login_Registration_Page(CAP)
        current_page.register_account_flow(generate_random_username(),self.variables['correct_password'],self.rand_email,UCOC=False)
        result = current_page.check_for_registration_error()
        try:
            self.assertTrue(result)
        except:
            current_page.close_page()