from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        # Locators
        self.driver = driver
        self.username_input_box = '//input[@name="user-name"]'
        self.password_input_box = '//input[@name="password"]'
        self.login_button = '//input[@type="submit"]'

    # Action Methods Below
    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_input_box).clear()
        self.driver.find_element(By.XPATH, self.username_input_box).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_input_box).clear()
        self.driver.find_element(By.XPATH, self.password_input_box).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()