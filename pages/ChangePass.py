def redirect_change_my_password():
    return "//*[@id='HeaderSV_LoginPanel2_lnkChangePassWord']"

def txt_password():
    return "//*[@id='NewPassword']"
    
def txt_confirm_password():
    return "//*[@id='ConfirmNewPassword']"

def btn_change():
    return "//*[@id='ChangePasswordPushButton']"

def btn_logout():
    return "//*[@id='Header1_LoginPanel2_lnkLogout']"