from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.product = '//div[text()="Sauce Labs Backpack"]'

    def click_product_link(self):
        self.driver.find_element(By.XPATH, self.product).click()

