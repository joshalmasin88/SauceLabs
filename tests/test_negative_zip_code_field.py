import pytest
from pages.loginPage import LoginPage
from pages.inventoryPage import InventoryPage
from pages.cartPage import CartPage
from pages.checkoutonePage import CheckoutonePage
from utils import utils
import time

@pytest.mark.usefixtures("test_setup")
class TestNegativeZipcodeField:
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login_page = LoginPage(driver)
        login_page.enter_username(utils.USERNAME)
        login_page.enter_password(utils.PASSWORD)
        login_page.click_login()
        time.sleep(5)


    def test_add_to_cart(self):
        driver = self.driver
        inventory_page = InventoryPage(driver)
        inventory_page.click_add_to_cart()
        inventory_page.click_cart_icon()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

    def test_add_info_checkout_one(self):
        driver = self.driver
        checkone_page = CheckoutonePage(driver)
        checkone_page.enter_first_name(utils.FIRSTNAME)
        checkone_page.enter_last_name(utils.LASTNAME)
        checkone_page.enter_zip(utils.NEGZIP)
        checkone_page.click_continue()