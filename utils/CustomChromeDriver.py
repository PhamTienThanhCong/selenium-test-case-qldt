from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def customChrome():
    option = Options()
    option.add_argument("--enable-extentions")

    driver = webdriver.Chrome(chrome_options=option, executable_path="./drivers/chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()

    print("[Open browser] Open google chrome browser")
    return driver
