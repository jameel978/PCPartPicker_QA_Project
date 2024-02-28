from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class Driver_instance:
    def __init__(self,driver):
        self._driver = driver

    def get_page_title(self):
        return self._driver.title

    def close_page(self):
        self._driver.close()

    def get_element_by_xpath(self, xpath):
        return self._driver.find_element(By.XPATH, xpath)

    def wait_and_get_element_by_xpath(self, xpath, sec=5):
        return WebDriverWait(self._driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def wait_and_get_elements_by_xpath(self, xpath, sec=5):
        return WebDriverWait(self._driver, sec).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def Find_and_click_on_element(self,element,click_using_javescript = False):
        if click_using_javescript:
            self._driver.execute_script("arguments[0].click();", self.wait_and_get_element_by_xpath(element))
        else:
            self.get_element_by_xpath(element).click()
        #self._driver.execute_script("arguments[0].scrollIntoView();", elem)
        #WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, element))).click()

    def Find_and_send_input_to_element(self,element,txt):
        self.wait_and_get_element_by_xpath(element).send_keys(txt)

    def is_element_found(self,elem,sec):
        try:
            self.wait_and_get_element_by_xpath(elem,sec=sec)
            return True
        except:
            return False
    def click_on_elem(self,elem):
        self._driver.execute_script("arguments[0].click();", elem)

    def drag_slider_elements(self,element,cur_price_elem,price):
        #ActionChains(self._driver).move_to_element(element).perform()
        #cur_price = float(cur_price_elem.text[1:])
        for i in range(30):
            self.drag_element_to_right(element, 1)
            time.sleep(0.3)
        for i in range(30):
            self.drag_element_to_left(element, 1)
            time.sleep(0.3)


    def drag_element_to_left(self,elem,speed=1):
        print("move left before", elem.location,end="")
        action = ActionChains(self._driver)
        action.drag_and_drop_by_offset(elem,-1, 0).perform()
        action.reset_actions()
        print(" After :",elem.location)
    def drag_element_to_right(self,elem,speed=1):
        #ActionChains(self._driver).click_and_hold(elem).move_by_offset(1*speed, 0).release().perform()
        action = ActionChains(self._driver)
        action.drag_and_drop_by_offset(elem,1, 0).perform()
        action.reset_actions()