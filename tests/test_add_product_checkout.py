import pytest
from utils import utils
from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage
from pages.productPage import ProductPage
from pages.cartPage import CartPage
from pages.checkoutonePage import CheckoutonePage
from pages.checkouttwoPage import CheckouttowPage
from pages.completeorderPage import CompleteorderPage
import time

@pytest.mark.usefixtures("test_setup")
class TestCheckout:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login_page = LoginPage(driver)
        login_page.enter_username(utils.USERNAME)
        login_page.enter_password(utils.PASSWORD)
        login_page.click_login()

    def test_add_to_cart(self):
        driver = self.driver
        inventory_page = InventoryPage(driver)

        inventory_page.click_product_link()

        product_page = ProductPage(driver)
        product_page.click_add_to_cart()
        product_page.click_cart()

        cart_page = CartPage(driver)
        cart_page.check_product_title()
        cart_page.check_product_price()
        cart_page.click_checkout()

    def test_checkout_process(self):
        driver = self.driver
        checkoutone_page = CheckoutonePage(driver)
        checkoutone_page.enter_first_name(utils.FIRSTNAME)
        checkoutone_page.enter_last_name(utils.LASTNAME)
        checkoutone_page.enter_zip(utils.ZIP)
        checkoutone_page.click_continue()

        checkouttwo_page = CheckouttowPage(driver)
        checkouttwo_page.check_product_title()
        checkouttwo_page.click_btn_finish()

        complete_order_page = CompleteorderPage(driver)
        complete_order_page.confirm_thanks_msg()