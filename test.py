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


def msg_result():
    return "//*[@id='LoginControl1_lblThong_bao']"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
broser = webdriver.Chrome(chrome_options=chrome_options ,executable_path="./drivers/chromedriver.exe")
broser.get('https://qldt.phenikaa-uni.edu.vn/')

account  = "20010886"
password = "Cong20023"

broser.find_element(By.XPATH, txt_username()).send_keys(account)
broser.find_element(By.XPATH, txt_password()).send_keys(password)
broser.find_element(By.XPATH, bnt_login()).click()

sleep(5)

if broser.find_element(By.XPATH, msg_result()):
    print("Login success")
else:
    print("Login fail")

broser.close()

