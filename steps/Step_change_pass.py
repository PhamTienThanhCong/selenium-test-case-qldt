from selenium.webdriver.common.by import By

from pages.ChangePass import txt_password, txt_confirm_password, btn_change, redirect_change_my_password


class stepChangePass:
    def __init__(self, driver):
        self.driver = driver

    def changePass(self, password, confirm_password):
        print("[Step] change password")
        self.clickGoToChangePass()
        self.inputUserName(password)
        self.inputPassword(confirm_password)
        self.clickButtonChangePass()

    # Action
    def inputUserName(self, password):
        print("[+] Input new password")
        self.get_txtPassword().send_keys(password)

    def inputPassword(self, confirm_password):
        print("[+] Input confirm new password")
        self.get_txtConfirmPassword().send_keys(confirm_password)

    def clickButtonChangePass(self):
        print("[+] Click button to submit")
        self.get_bntLogin().click()

    def clickGoToChangePass(self):
        print("[+] Click button to change password")
        self.get_btnToChange().click()

    # Get element
    def get_txtPassword(self):
        return self.driver.find_element(By.XPATH, txt_password())

    def get_txtConfirmPassword(self):
        return self.driver.find_element(By.XPATH, txt_confirm_password())

    def get_bntLogin(self):
        return self.driver.find_element(By.XPATH, btn_change())

    def get_btnToChange(self):
        return self.driver.find_element(By.XPATH, redirect_change_my_password())

