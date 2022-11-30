from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.ChangeInfor import txt_email, txt_sdtCaNhanGet, txt_sdtGiaDinhGet, txt_diaChi_GiaDinh, txt_Noi_O_get


class verifyMyAccount:
    def __init__(self, driver):
        self.driver = driver

    def getInfo(self):
        email = self.driver.find_element(By.XPATH, txt_email()).text
        sdtCaNhan = self.driver.find_element(By.XPATH, txt_sdtCaNhanGet()).text
        sdtGiaDinh = self.driver.find_element(By.XPATH, txt_sdtGiaDinhGet()).text
        diaChiGiaDinh = self.driver.find_element(By.XPATH, txt_diaChi_GiaDinh()).text
        noiO = self.driver.find_element(By.XPATH, txt_Noi_O_get()).text
        print([email, sdtCaNhan, sdtGiaDinh, diaChiGiaDinh, noiO])
        return [email, sdtCaNhan, sdtGiaDinh, diaChiGiaDinh, noiO]