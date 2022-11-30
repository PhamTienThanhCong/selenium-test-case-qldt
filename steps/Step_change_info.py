from selenium.webdriver.common.by import By

from pages.ChangeInfor import redirect_page, txt_email, txt_sdtCaNhan, txt_sdtGiaDinh, txt_diaChi_GiaDinh, txt_Noi_O, btn_save


class stepChangeInfo:
    def __init__(self, driver):
        self.driver = driver

    def changeInfo(self, email, sdtCaNhan, sdtGiaDinh, dia_chi_nha, dia_chi_lien_lac):
        print("[Step] change my info")
        self.get_redirect_page().click()
        self.inputEmail(email)
        self.inputSdtCaNhan(sdtCaNhan)
        self.inputSdtGiaDinh(sdtGiaDinh)
        self.inputDiaChiGiaDinh(dia_chi_lien_lac)
        self.inputNoiO(dia_chi_nha)
        self.clickButtonChange()

    # Action
    def inputEmail(self, email):
        print("[+] Input new password")
        self.get_txtEmail().clear()
        self.get_txtEmail().send_keys(email)

    def inputSdtCaNhan(self, sdtCaNhan):
        print("[+] Input new my phone number")
        self.get_txtSdtCaNhan().clear()
        self.get_txtSdtCaNhan().send_keys(sdtCaNhan)

    def inputSdtGiaDinh(self, sdtGiaDinh):
        print("[+] Input new home phone number")
        self.get_txtSdtGiaDinh().clear()
        self.get_txtSdtGiaDinh().send_keys(sdtGiaDinh)

    def inputDiaChiGiaDinh(self, diaChiGiaDinh):
        print("[+] Input new home address")
        self.get_txtDiaChiGiaDinh().clear()
        self.get_txtDiaChiGiaDinh().send_keys(diaChiGiaDinh)

    def inputNoiO(self, noiO):
        print("[+] Input new home address")
        self.get_txtNoiO().clear()
        self.get_txtNoiO().send_keys(noiO)

    def clickButtonChange(self):
        print("[+] Click button to change password")
        self.get_btnSave().click()

    # Get element
    def get_txtEmail(self):
        return self.driver.find_element(By.XPATH, txt_email())
    
    def get_txtSdtCaNhan(self):
        return self.driver.find_element(By.XPATH, txt_sdtCaNhan())
    
    def get_txtSdtGiaDinh(self):
        return self.driver.find_element(By.XPATH, txt_sdtGiaDinh())
    
    def get_txtDiaChiGiaDinh(self):
        return self.driver.find_element(By.XPATH, txt_diaChi_GiaDinh())
    
    def get_txtNoiO(self):
        return self.driver.find_element(By.XPATH, txt_Noi_O())
    
    def get_btnSave(self):
        return self.driver.find_element(By.XPATH, btn_save())
    
    def get_redirect_page(self):
        return self.driver.find_element(By.XPATH, redirect_page())

