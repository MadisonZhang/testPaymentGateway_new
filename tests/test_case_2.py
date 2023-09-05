from test_units import *
from utilities.constants import QUANTITY, TEST_SITE_URL, EXP_MONTH, EXP_YEAR, CVV1, INVALID_CARD_NUMBER
from utilities.page_objects.index_page import IndexPage
from utilities.page_objects.process_page import ProcessPage
import time

class TestPaymentGateway:
    # Test case 2 (Verifying Card Number Field: Blank or invalid card number digits)
    def test_card_info(self, driver):
        test_quantity = QUANTITY[8]
        test_amount = test_quantity * 20
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.select_quantity((test_quantity - 1))
        index_page.wait_and_click_submit_button()

        process_page = ProcessPage(driver)
        price_label = process_page.payment_amount()
        assert price_label.__contains__(str(test_amount)), "Items ready to check out"

        process_page.fill_card_number("")
        process_page.select_exp_month(EXP_MONTH[12])
        process_page.select_exp_year(EXP_YEAR[12])
        process_page.fill_CVV(CVV1)
        time.sleep(1)
        card_number_alert_label_1 = "Field must not be blank"
        assert card_number_alert_label_1 == process_page.invalid_card_number_alert_1(), f"Alert message: {process_page.invalid_card_number_alert_1()} successfully displayed on the page"
        process_page.fill_card_number(INVALID_CARD_NUMBER)
        time.sleep(1)
        process_page.find_submit_button_and_click()
        card_number_alert_label_2 = "16 digits"
        assert card_number_alert_label_2 in process_page.invalid_card_number_alert_2(), f"Alert message: {process_page.invalid_card_number_alert_2()} successfully displayed on popped out window"
