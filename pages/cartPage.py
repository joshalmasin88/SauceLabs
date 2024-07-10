from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_title_xpath = '//div[text()="Sauce Labs Backpack"]'
        self.product_price_xpath = '//div[@class="inventory_item_price"]'
        self.checkout_button_xpath = '//button[@data-test="checkout"]'

    def check_product_title(self):
        product_title = self.driver.find_element(By.XPATH, self.product_title_xpath).text
        assert product_title == "Sauce Labs Backpack"

    def check_product_price(self):
        product_price = self.driver.find_element(By.XPATH, self.product_price_xpath).text
        assert product_price == "$29.99"

    def click_checkout(self):
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()