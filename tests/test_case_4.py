from test_units import *
from utilities.constants import QUANTITY, TEST_SITE_URL, EXP_MONTH, CVV1, VALID_CARD_NUMBER, \
    PAYMENT_PROCESS_URL
from utilities.page_objects.index_page import IndexPage
from utilities.page_objects.process_page import ProcessPage
import time

class TestPaymentGateway:
    # Test case 3 (Verifying Expiration Year Field Validation)
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

        process_page.fill_card_number(VALID_CARD_NUMBER)
        process_page.select_exp_month(EXP_MONTH[12])
        process_page.fill_CVV(CVV1)
        time.sleep(2)
        process_page.find_submit_button_and_click()
        # Assert that the form submission doesn't proceed (due to required field)
        assert PAYMENT_PROCESS_URL in process_page.get_current_url()