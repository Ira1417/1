from base_page import BasePage
from locators import AuthLocators, RegLocators, RecovLocators
import time,os

class AuthPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/auth"
        driver.get(url)

        self.btn_phone = driver.find_element(*AuthLocators.AUTH_BTN_PHONE)
        self.btn_email = driver.find_element(*AuthLocators.AUTH_BTN_EMAIL)
        self.btn_login = driver.find_element(*AuthLocators.AUTH_BTN_LOGIN)
        self.btn_ls = driver.find_element(*AuthLocators.AUTH_BTN_LS)
        self.btn_vk = driver.find_element(*AuthLocators.AUTH_VK)
        self.btn_ok = driver.find_element(*AuthLocators.AUTH_OK)
        self.btn_mail = driver.find_element(*AuthLocators.AUTH_MAIL)
        self.btn_google = driver.find_element(*AuthLocators.AUTH_GOOGLE)
        self.btn_ya = driver.find_element(*AuthLocators.AUTH_YA)
        self.link_fogot_pass = driver.find_element(*AuthLocators.FOGOT_PASS)
        self.link_register = driver.find_element(*AuthLocators.REGISTER)
        self.link_auth_user_agreement = driver.find_element(*AuthLocators.AUTH_USER_AGREEMENT)
        self.link_footer_user_agreement = driver.find_element(*AuthLocators.FOOTER_AGREEMENT)
        self.username = driver.find_element(*AuthLocators.AUTH_INPUT_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_INPUT_PASSWORD)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        time.sleep(3)



    def btn_phone_click(self):
        self.btn_phone.click()
    time.sleep(2)

    def btn_email_click(self):
        self.btn_email.click()
    time.sleep(2)

    def btn_login_click(self):
        self.btn_login.click()
    time.sleep(2)

    def btn_ls_click(self):
        self.btn_ls.click()
    time.sleep(2)

    def btn_vk_click(self):
        self.btn_vk.click()
    time.sleep(2)

    def btn_ok_click(self):
        self.btn_ok.click()
    time.sleep(2)

    def btn_mail_click(self):
        self.btn_mail.click()
    time.sleep(2)

    def btn_google_click(self):
        self.btn_google.click()
    time.sleep(2)

    def btn_ya_click(self):
        self.btn_ya.click()
    time.sleep(2)

    def link_fogot_pass_click(self):
        self.link_fogot_pass.click()
    time.sleep(2)

    def link_register_click(self):
         self.link_register.click()
    time.sleep(2)

    def link_auth_user_agreement_click(self):
        self.link_auth_user_agreement.click()
    time.sleep(2)

    def link_footer_user_agreement_click(self):
        self.link_footer_user_agreement.click()
    time.sleep(2)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()
    time.sleep(3) #ждем реакции


class RegPage(AuthPage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=c0660f76-7bb7-44a8-9df9-b3198f38f550&client_id=account_b2c&tab_id=MvW51vOXCHE"
        driver.get(url)


        self.name = driver.find_element(*RegLocators.REG_NAME)
        self.surname = driver.find_element(*RegLocators.REG_SURNAME)
        self.email_phone = driver.find_element(*RegLocators.REG_EMAIL_PHONE)
        self.password = driver.find_element(*RegLocators.REG_PASSWORD)
        self.repeat_pass = driver.find_element(*RegLocators.REG_REPEAT_PASS)
        self.btn = driver.find_element(*RegLocators.REG_BTN)
        self.link_reg_user_agreement = driver.find_element(*RegLocators.REG_USER_AGREEMENT)
        time.sleep(3)


    def link_reg_user_agreement_click(self):
        self.link_reg_user_agreement()
    time.sleep(2)

    def enter_name(self, value):
        self.name.send_keys(value)

    def enter_surname(self, value):
        self.surname.send_keys(value)

    def enter_email_phone(self, value):
        self.email_phone.send_keys(value)

    def enter_pass(self, value):
        self.password.send_keys(value)

    def enter_repeat_pass(self, value):
        self.repeat_pass.send_keys(value)

    def btn_click(self):
        self.btn.click()
    time.sleep(3)


class RecovPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials"
        driver.get(url)


        self.btn_phone = driver.find_element(*RecovLocators.RECOV_BTN_PHONE)
        self.btn_email = driver.find_element(*RecovLocators.RECOV_BTN_EMAIL)
        self.btn_login = driver.find_element(*RecovLocators.RECOV_BTN_LOGIN)
        self.btn_ls = driver.find_element(*RecovLocators.RECOV_BTN_LS)
        self.username = driver.find_element(*RecovLocators.RECOV_USERNAME)
        self.btn = driver.find_element(*RecovLocators.RECOV_BTN)
        self.link_back_to_auth = driver.find_element(*RecovLocators.BACK_TO_AUTH)
        time.sleep(3)


    def btn_phone_click(self):
        self.btn_phone.click()
    time.sleep(2)

    def btn_email_click(self):
        self.btn_email.click()
    time.sleep(2)

    def btn_login_click(self):
        self.btn_login.click()
    time.sleep(2)

    def btn_ls_click(self):
        self.btn_ls.click()
    time.sleep(2)

    def link_back_to_auth_click(self):
        self.link_back_to_auth()
    time.sleep(3)

    def enter_username(self, value):
        self.username.send_keys(value)
    time.sleep(3)

    def btn_click(self):
        self.btn.click()
    time.sleep(3)
