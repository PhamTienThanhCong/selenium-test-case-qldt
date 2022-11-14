import unittest

from utils.CustomChromeDriver import customChrome
from selenium.webdriver.common.by import By
from reports.Runner import HTMLTestRunner
from parameterized import parameterized
from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from verifys.Verify_login import verifyLogin
from steps.Step_change_pass import stepChangePass

# import Alert 
from selenium.webdriver.common.alert import Alert

from pages.ChangePass import btn_logout

dataTests = readDatatest().dataTestLogin('./dataTest/Data_testChangePass.xlsx')

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        self.browser = customChrome()
        self.browser.get("https://qldt.phenikaa-uni.edu.vn/")

    def tearDown(self):
        self.browser.quit()
        print("========== [ End Test ] ========== \n")

    @parameterized.expand(dataTests)
    def test_info(self, stt, Username, Password, new_pass, confirm_pass, message):
        stepLogin(self.browser).login(Username, Password)
        actualResult = verifyLogin(self.browser).login()

        self.assertIn("done", actualResult)

        stepChangePass(self.browser).changePass(new_pass, confirm_pass)

        # get alert message and verify
        alert = Alert(self.browser)
        alert_text = alert.text
        alert.accept()

        self.assertEqual(alert_text, message)

        print("[+] change pass success")
        # verify change password success

        print("[+] logout")

        self.browser.find_element(By.XPATH, btn_logout()).click()

        # login with new password
        print("[+] login with new password")
        stepLogin(self.browser).login(Username, new_pass)
        self.assertIn("done", actualResult)

        print("Test change password success")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(report_title = "đổi mật khẩu"))
