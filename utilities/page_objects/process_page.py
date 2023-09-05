from utilities.constants import MAX_WAIT_INTERVAL
from utilities.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProcessPage(BasePage):
    PAY_AMOUNT = (By.XPATH, "//div[@class='6u 12u$(xsmall)']/font[2]")
    CARD_NUMBER = (By.ID,"card_nmuber")
    EXP_MONTH = (By.ID,"month")
    EXP_YEAR = (By.ID,"year")
    CVV = (By.ID,"cvv_code")
    SUBMIT_LINK = (By.NAME,"submit")
    CARD_NUMBER_ALERT = (By.ID, "message1")
    CVV_ALERT = (By.ID, "message2")

    def payment_amount(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,self.PAY_AMOUNT).text

    def fill_card_number(self,card_num):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,self.CARD_NUMBER).send_keys(card_num)

    def select_exp_month(self,exp_month):
        self.select_by_index(MAX_WAIT_INTERVAL,self.EXP_MONTH,exp_month)

    def select_exp_year(self,exp_year):
        self.select_by_index(MAX_WAIT_INTERVAL,self.EXP_YEAR,exp_year)

    def fill_CVV(self,cvv_num):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,self.CVV).send_keys(cvv_num)

    def find_submit_button_and_click(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.SUBMIT_LINK).click()

    def invalid_card_number_alert_1(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,self.CARD_NUMBER_ALERT).text

    def invalid_card_number_alert_2(self):
        return self.explicitly_wait_alert(MAX_WAIT_INTERVAL).text

    def cvv_alert(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, self.CVV_ALERT).text