from Infra.Driver_instance import Driverinstance
import time

class Login_Registration_Page(Driverinstance):
    # HOMEPAGE
    # https://pcpartpicker.com/
    LOGIN_BUTTON = "//ul[@class='nav__account nav__account--desktop list-unstyled']/li[@class='nav__account--login']"
    REGISTER_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--register']//a[normalize-space()='Register']"

    # AFTER LOGIN_BUTTON
    LOGOUT_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--logout']//a[normalize-space()='Log Out']"
    SAVED_PARTS_BUTTON = "//ul[@role='presentation']//a[contains(text(),'Saved Parts Lists')]"
    FAVORITE_PART_BUTTON = "//ul[@role='presentation']//li[@class='nav__account--favorites']//a[contains(text(),'Favorite Parts')]"


    # LOGIN_PAGE
    USER_INPUT = "//input[@id='id_username']"
    PASSWORD_INPUT = "//input[@id='id_password']"
    SUBMIT_BUTTON = "//input[@id='input_recaptcha']"
    WRONG_CREDENTAILS = "//p[normalize-space()='Invalid username or password. Please try again.']"

    # REGISTRATION_PAGE
    EMAIL_INPUT = "//input[@id='id_email']"
    EMAIL_INPUT_SECOND = "//input[@id='id_email2']"
    FIRST_PASSWORD_INPUT_REGISTRATION = "//input[@id='id_password1']"
    SECOND_PASSWORD_INPUT_REGISTRATION = "//input[@id='id_password2']"
    ACCEPT_TOS_CHECKBOX = "//label[@for='id_accept_tos']"
    ACCEPT_UCOC_CHECKBOX = "//label[@for='id_accept_ucoc']"
    COMPLETE_REGISTRATION = "//input[@id='input_recaptcha']"
    REGISTRATION_IS_COMPLETED = "//h1[normalize-space()='Registration Complete']"

    GENERAL_TEXT_ERROR = "//p[@class='text-error']"
    ALREADY_REGISTERED_USERNAME = "//p[normalize-space()='A user with that username already exists.']"
    INVALID_USERNAME = "//p[contains(text(),'This value may contain only letters, numbers and @')]"
    ALREADY_REGISTERED_EMAIL = "//p[contains(text(),'This email address is already in use. Please suppl')]"
    INVALID_EMAIL_ERROR = "//p[@class='text-error'][normalize-space()='Enter a valid email address.']"
    NOT_MATCHING_EMAIL = '(//p[normalize-space()="The two email fields didn\'t match."])'
    NOT_MATCHING_PASSWORD = '//p[normalize-space()="The two password fields didn\'t match."]'

    PAGE_URL = "https://pcpartpicker.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_url(self.PAGE_URL)
        time.sleep(3)
        self.refresh_driver()
        time.sleep(3)
        self.print_html_page()


    def account_login_flow(self, username, password):
        self.Find_and_click_on_element(self.LOGIN_BUTTON)
        self.Find_and_send_input_to_element(self.USER_INPUT, username)
        self.Find_and_send_input_to_element(self.PASSWORD_INPUT, password)
        self.Find_and_click_on_element(self.SUBMIT_BUTTON)

    def register_account_flow(self, username, password, email, email_repeat=True, password_repeat=True, TOS=True,
                              UCOC=True):
        if isinstance(email_repeat, bool):
            email_repeat = email
        if isinstance(password_repeat, bool):
            password_repeat = password
        self.Find_and_click_on_element(self.REGISTER_BUTTON)
        self.Find_and_send_input_to_element(self.USER_INPUT, username)
        self.Find_and_send_input_to_element(self.EMAIL_INPUT, email)
        self.Find_and_send_input_to_element(self.EMAIL_INPUT_SECOND, email_repeat)
        self.Find_and_send_input_to_element(self.FIRST_PASSWORD_INPUT_REGISTRATION, password)
        self.Find_and_send_input_to_element(self.SECOND_PASSWORD_INPUT_REGISTRATION, password_repeat)
        if TOS:
            self.Find_and_click_on_element(self.ACCEPT_TOS_CHECKBOX)
        if UCOC:
            self.Find_and_click_on_element(self.ACCEPT_UCOC_CHECKBOX)
        self.Find_and_click_on_element(self.COMPLETE_REGISTRATION)

    def check_for_registration_error(self):
        return self.is_element_found(self.GENERAL_TEXT_ERROR, sec=3)

    def check_for_already_registered_username_error(self):
        return self.is_element_found(self.ALREADY_REGISTERED_USERNAME, sec=3)

    def check_for_invalid_username(self):
        return self.is_element_found(self.INVALID_USERNAME, sec=3)

    def check_for_invalid_email(self):
        return self.is_element_found(self.INVALID_EMAIL_ERROR, sec=3)

    def check_for_already_registered_email(self):
        return self.is_element_found(self.ALREADY_REGISTERED_EMAIL, sec=3)

    def check_for_not_matching_email(self):
        return self.is_element_found(self.NOT_MATCHING_EMAIL, sec=3)

    def check_for_not_matching_password(self):
        return self.is_element_found(self.NOT_MATCHING_PASSWORD, sec=3)

    def check_if_registration_is_complete(self):
        return self.is_element_found(self.REGISTRATION_IS_COMPLETED, sec=3)

    def check_if_user_is_logged_in(self):
        return self.is_element_found(self.LOGOUT_BUTTON, sec=3)

    def check_if_user_entred_wrong_credentials(self):
        return self.is_element_found(self.WRONG_CREDENTAILS, sec=3)