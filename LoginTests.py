import unittest

from utils.CustomChromeDriver import customChrome
from reports.Runner import HTMLTestRunner
from parameterized import parameterized
from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from verifys.Verify_login import verifyLogin

dataTests = readDatatest().dataTestLogin("./dataTest/Data_testLogin.xlsx") 

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        self.browser = customChrome()
        self.browser.get("https://qldt.phenikaa-uni.edu.vn/")

    def tearDown(self):
        self.browser.quit()
        print("========== [ End Test ] ========== \n")

    @parameterized.expand(dataTests)
    def test_login(self, no, username, password, ValueCheck):
        stepLogin(self.browser).login(username, password)

        print("[Step] Check login " + ValueCheck)

        self.assertIn(ValueCheck, verifyLogin(self.browser).login())

        print("Test is successful")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(report_title = "Đăng nhập"))
