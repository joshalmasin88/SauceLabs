from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_cart_btn_id = 'add-to-cart'
        self.cart_xpath = '//a[@data-test="shopping-cart-link"]'

    def click_add_to_cart(self):
        self.driver.find_element(By.ID, self.add_cart_btn_id).click()

    def click_cart(self):
        self.driver.find_element(By.XPATH, self.cart_xpath).click()
