import unittest

from utils.CustomChromeDriver import customChrome
from selenium.webdriver.common.by import By
from reports.Runner import HTMLTestRunner
from parameterized import parameterized
from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from verifys.Verify_login import verifyLogin
from verifys.Verify_myInfor import verifyMyinfor

from pages.MyInfor import redirect_my_account

dataTests = readDatatest().dataTestLogin('./dataTest/Data_testCheckAccount.xlsx')

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        self.browser = customChrome()
        self.browser.get("https://qldt.phenikaa-uni.edu.vn/")

    def tearDown(self):
        self.browser.quit()
        print("========== [ End Test ] ========== \n")

    @parameterized.expand(dataTests)
    def test_info(self, stt, username, password, HoTen, NgaySinh, GioiTinh):
        stepLogin(self.browser).login(username, password)
        actualResult = verifyLogin(self.browser).login()

        self.assertIn("done", actualResult)

        print("[Step] Test my infor")
        print("[+] go to my account")

        self.browser.find_element(By.XPATH, redirect_my_account()).click()
        resultAccount = verifyMyinfor(self.browser).getInfo()
        data_type = ["Mssv", "Họ Tên", "Ngày Sinh", "Giới Tính"]

        for i in range(0, len(resultAccount)):
            self.assertEqual(resultAccount[i], [username, HoTen, NgaySinh, GioiTinh][i])
            print("[+] Check " + data_type[i] + " is correct")
        print("Test is successful")




if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(report_title = "xem thông tin cá nhân"))
