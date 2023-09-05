from utilities.constants import MAX_WAIT_INTERVAL
from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class IndexPage(BasePage):
    QUANTITY_SELECT = (By.NAME,"quantity")
    BUY_NOW_LINK = (By.XPATH, "//input[@value='Buy Now']")

    def select_quantity(self,quantity):
        self.select_by_index(MAX_WAIT_INTERVAL,self.QUANTITY_SELECT,quantity)

    def wait_and_click_submit_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,self.BUY_NOW_LINK).click()