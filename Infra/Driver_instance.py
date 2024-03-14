from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class Driverinstance:
    def __init__(self,cap):
        driver = cap[0](**cap[1])
        # Changing the property of the navigator value for webdriver to undefined
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self._driver = driver

    def print_html_page(self):
        # Get the page source (HTML)
        html = self._driver.page_source
        # Print the HTML
        print(html)
        self._driver.save_screenshot('test.png')
    def get_page_title(self):
        return self._driver.title

    def refresh_driver(self):
        self._driver.refresh()

    def close_page(self):
        self._driver.close()

    def get_element_by_xpath(self, xpath):
        return self._driver.find_element(By.XPATH, xpath)

    def wait_and_get_element_by_xpath(self, xpath, sec=5):
        return WebDriverWait(self._driver, sec).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def wait_and_get_elements_by_xpath(self, xpath, sec=5):
        return WebDriverWait(self._driver, sec).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def Find_and_click_on_element(self, element, click_using_javescript=False):
        if click_using_javescript:
            self._driver.execute_script("arguments[0].click();", self.wait_and_get_element_by_xpath(element))
        else:
            self.get_element_by_xpath(element).click()
        # self._driver.execute_script("arguments[0].scrollIntoView();", elem)
        # WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable((By.XPATH, element))).click()

    def Find_and_send_input_to_element(self, element, txt):
        self.wait_and_get_element_by_xpath(element).send_keys(txt)

    def is_element_found(self, elem, sec):
        try:
            self.wait_and_get_element_by_xpath(elem, sec=sec)
            return True
        except:
            return False

    def click_on_elem(self, elem):
        #self._driver.execute_script("arguments[0].scrollIntoView();", elem)
        self._driver.execute_script("arguments[0].click();", elem)



    def drag_element_to_location(self, element, wanted_location, cur_location):
        if wanted_location > cur_location:
            self.drag_element_to_right(element,speed = wanted_location - cur_location)
        elif wanted_location < cur_location:
            self.drag_element_to_left(element,speed = cur_location - wanted_location)
        time.sleep(0.05)


    def drag_element_to_left(self, elem, speed=1):
        ActionChains(self._driver).click_and_hold(elem).move_by_offset(-0.74*speed, 0).release().perform()

    def drag_element_to_right(self, elem, speed=1):
        ActionChains(self._driver).click_and_hold(elem).move_by_offset(1*speed, 0).release().perform()
    def close_browser(self):
        self._driver.close()

    def quit(self):
        self._driver.quit()

    def go_to_url(self,url):
        self._driver.get(url)
