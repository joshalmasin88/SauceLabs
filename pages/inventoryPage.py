from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.product = '//div[text()="Sauce Labs Backpack"]'
        self.product_add_to_cart_xpath = '//button[@id="add-to-cart-sauce-labs-backpack"]'
        self.cart_xpath = '//a[@data-test="shopping-cart-link"]'

    def click_product_link(self):
        self.driver.find_element(By.XPATH, self.product).click()

    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH, self.product_add_to_cart_xpath).click()

    def click_cart_icon(self):
        self.driver.find_element(By.XPATH, self.cart_xpath).click()