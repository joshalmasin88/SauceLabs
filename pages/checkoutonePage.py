from selenium.webdriver.common.by import By


class CheckoutonePage:

    def __init__(self, driver):
        self.driver = driver
        self.firstName_xpath = '//input[@name="firstName"]'
        self.lastName_xpath = '//input[@name="lastName"]'
        self.zip_xpath = '//input[@id="postal-code"]'
        self.continue_btn_xpath = '//input[@id="continue"]'

    def enter_first_name(self, firstname):
        self.driver.find_element(By.XPATH, self.firstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstName_xpath).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(By.XPATH, self.lastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastName_xpath).send_keys(lastname)

    def enter_zip(self, zip):
        self.driver.find_element(By.XPATH, self.zip_xpath).clear()
        self.driver.find_element(By.XPATH, self.zip_xpath).send_keys(zip)

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()