from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as df
import random

def txt_username():
    return "//input[@name = 'LoginControl1$txtusername']"


def txt_password():
    return "//input[@name = 'LoginControl1$txtpassword']"


def bnt_login():
    return "//input[@id = 'LoginControl1_btnDangNhap']"

def redirect_change_my_password():
    return "//*[@id='HeaderSV_LoginPanel2_lnkChangePassWord']"

def txt_new_password():
    return "//*[@id='NewPassword']"
def txt_confirm_password():
    return "//*[@id='ConfirmNewPassword']"

def btn_change():
    return "//*[@id='ChangePasswordPushButton']"

def btn_logout():
    return "//*[@id='HeaderSV_LoginPanel2_lnkLogout']"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
broser = webdriver.Chrome(chrome_options=chrome_options ,executable_path="./drivers/chromedriver.exe")
broser.get('https://qldt.phenikaa-uni.edu.vn/')

account  = "20010886"
password = "Cong2002"

broser.find_element(By.XPATH, txt_username()).send_keys(account)
broser.find_element(By.XPATH, txt_password()).send_keys(password)
broser.find_element(By.XPATH, bnt_login()).click()

broser.find_element(By.XPATH, redirect_change_my_password()).click()

sleep(5)

broser.close()

