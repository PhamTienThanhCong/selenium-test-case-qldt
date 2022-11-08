from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Page_login import msg_result


class verifyLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.waitLoginFinish()
        contentMessage = self.waitLoginFinish()

        return contentMessage

    # Get element
    def waitLoginFinish(self):
        print("[+] Wait login finish")
        if self.driver.find_element(By.XPATH, msg_result()).text:
            print("Login success")
            return self.driver.find_element(By.XPATH, msg_result()).text
        else:
            print("Login fail")
            return True
        # return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, msg_result())))
