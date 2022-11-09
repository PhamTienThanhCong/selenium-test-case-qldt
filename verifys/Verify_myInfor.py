from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.MyInfor import txt_gioiTinh, txt_hoTen, txt_maSv, txt_ngaySinh


class verifyMyinfor:
    def __init__(self, driver):
        self.driver = driver

    def getInfo(self):
        mssv = self.driver.find_element(By.XPATH, txt_maSv()).text
        hoten = self.driver.find_element(By.XPATH, txt_hoTen()).text
        ngaysinh = self.driver.find_element(By.XPATH, txt_ngaySinh()).text
        gioitinh = self.driver.find_element(By.XPATH, txt_gioiTinh()).text

        return [mssv, hoten, ngaysinh, gioitinh]

        # return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, msg_result())))