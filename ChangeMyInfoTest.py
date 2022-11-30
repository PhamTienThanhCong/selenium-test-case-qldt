import unittest

from utils.CustomChromeDriver import customChrome
from selenium.webdriver.common.by import By
from reports.Runner import HTMLTestRunner
from parameterized import parameterized
from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from verifys.Verify_login import verifyLogin
from steps.Step_change_info import stepChangeInfo
from verifys.Verify_my_account import verifyMyAccount

# import Alert 
from selenium.webdriver.common.alert import Alert

from pages.MyInfor import redirect_my_account

dataTests = readDatatest().dataTestLogin('./dataTest/Data_testChangeAccount.xlsx')

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [Begin Test] ==========")
        self.browser = customChrome()
        self.browser.get("https://qldt.phenikaa-uni.edu.vn/")

    def tearDown(self):
        self.browser.quit()
        print("========== [ End Test ] ========== \n")

    @parameterized.expand(dataTests)
    def test_info(self, stt, Username, Password, new_email, sdt_ca_nhan, sdt_gia_dinh, dia_chi_lien_lac, dia_chi_nha, result):
        stepLogin(self.browser).login(Username, Password)
        actualResult = verifyLogin(self.browser).login()

        self.assertIn("done", actualResult)

        stepChangeInfo(self.browser).changeInfo(new_email, sdt_ca_nhan, sdt_gia_dinh, dia_chi_nha, dia_chi_lien_lac)

        # get alert message and verify
        alert = Alert(self.browser)
        alert_text = alert.text
        alert.accept()

        self.assertEqual(alert_text, result)

        print("[+] change the information successfully")
        # verify change password successfully

        print("[Step] Test my infor")

        print("[+] go to my account")
        self.browser.find_element(By.XPATH, redirect_my_account()).click()

        resultAccount = verifyMyAccount(self.browser).getInfo()
        data_type = ["Email", "Số Điện Thoại Cá Nhân", "Số Điện Thoại Gia Đình", "Địa Chỉ Liên Lạc", "Địa Chỉ Nhà"]

        for i in range(0, len(resultAccount)):
            self.assertEqual(resultAccount[i], [new_email, sdt_ca_nhan, sdt_gia_dinh, dia_chi_lien_lac, dia_chi_nha][i])
            print("[+] Check " + data_type[i] + " is correct")

        print("Test my info")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(report_title = "đổi mật khẩu"))
