from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url
    def navigate_to(self,url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self,interval,locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))

    def select_by_index(self,interval,locator_type_and_locator_tuple,index):
        dropdown_element = self.explicitly_wait_and_find_element(interval,locator_type_and_locator_tuple)
        dropdown = Select(dropdown_element)
        dropdown.select_by_index(index)

    def refresh_page(self, driver):
        driver.refresh()

    def explicitly_wait_alert(self,interval):
        return WebDriverWait(self.driver, interval).until(ec.alert_is_present())

