from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Page_login import msg_result, msg_result_error


class verifyLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        contentMessage = self.waitLoginFinish()

        return contentMessage

    # Get element
    def waitLoginFinish(self):
        print("[+] Wait login finish")
        # get url after login
        url = self.driver.current_url
        if url != "https://qldt.phenikaa-uni.edu.vn/":
            print("[+] Login success")
            return "done"
        else:
            print("[+] Login fail")
            return "fail"
        # return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, msg_result())))
