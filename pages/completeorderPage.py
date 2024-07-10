from selenium.webdriver.common.by import By


class CompleteorderPage:

    def __init__(self, driver):
        self.driver = driver
        self.thank_you_msg_xpath = '//h2[contains(text(), "Thank you for your order!")]'

    def confirm_thanks_msg(self):
        thank_you_msg = self.driver.find_element(By.XPATH, self.thank_you_msg_xpath).text
        assert thank_you_msg == "Thank you for your order!"