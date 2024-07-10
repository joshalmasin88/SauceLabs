from selenium.webdriver.common.by import By


class CheckouttowPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_title_xpath = '//div[text()="Sauce Labs Backpack"]'
        self.finished_button_xpath = '//button[@id="finish"]'

    def check_product_title(self):
        product_title = self.driver.find_element(By.XPATH, self.product_title_xpath).text
        assert product_title == "Sauce Labs Backpack"

    def click_btn_finish(self):
        self.driver.find_element(By.XPATH, self.finished_button_xpath).click()
