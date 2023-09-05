from utilities.constants import MAX_WAIT_INTERVAL
from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class PaymentSuccessful(BasePage):
    ORDER_ID = (By.XPATH,"//table[@class='alt access']/tbody/tr[1]/td[2]/h3")
    HOME_LINK = (By.PARTIAL_LINK_TEXT,"Home")

    def get_order_id(self):
        order_id = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,self.ORDER_ID).text
        return order_id

    def find_home_button_and_click(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,self.HOME_LINK).click()