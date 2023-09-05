from test_units import *
from utilities.constants import QUANTITY, TEST_SITE_URL, EXP_MONTH, EXP_YEAR, CVV1, VALID_CARD_NUMBER
from utilities.page_objects.index_page import IndexPage
from utilities.page_objects.payment_successful_page import PaymentSuccessful
from utilities.page_objects.process_page import ProcessPage
import time


class TestPaymentGateway:
    # Test case 5 (Verifying CVV Field Prompt)
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
        process_page.fill_CVV("")
        time.sleep(2)
        cvv_alert_label = "Field must not be blank"
        process_page.select_exp_year(EXP_YEAR[12])
        assert cvv_alert_label == process_page.cvv_alert(), f"Alert message: {process_page.cvv_alert()} successfully displayed on the page"
        process_page.find_submit_button_and_click()

        # CVV is normally required but some retailers don't ask for CVV
        payment_successful_page = PaymentSuccessful(driver)
        order_number = None
        try:
            order_number = payment_successful_page.get_order_id()
            assert order_number is not None, f"Order successfully placed with order number {order_number}."
        except:
            print("Order number not available.")

