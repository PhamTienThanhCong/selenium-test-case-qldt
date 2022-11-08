def txt_username():
    return "//input[@name = 'LoginControl1$txtusername']"


def txt_password():
    return "//input[@name = 'LoginControl1$txtpassword']"


def bnt_login():
    return "//button[@type = 'LoginControl1$btnDangNhap']"


def msg_result():
    return "//div[@id = 'LoginControl1_lblThong_bao']/div"
