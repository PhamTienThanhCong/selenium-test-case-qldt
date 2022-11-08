from selenium.webdriver.common.by import By

from pages.Page_login import txt_username, txt_password, bnt_login


class stepLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        print("[Step] Login")
        self.inputUserName(username)
        self.inputPassword(password)
        self.clickButtonLogin()

    # Action
    def inputUserName(self, username):
        print("[+] Input username")
        self.get_txtUsername().send_keys(username)

    def inputPassword(self, password):
        print("[+] Input password")
        self.get_txtpassword().send_keys(password)

    def clickButtonLogin(self):
        print("[+] Click button login")
        self.get_bntLogin().click()

    # Get element
    def get_txtUsername(self):
        return self.driver.find_element(By.XPATH, txt_username())

    def get_txtpassword(self):
        return self.driver.find_element(By.XPATH, txt_password())

    def get_bntLogin(self):
        return self.driver.find_element(By.XPATH, bnt_login())
