from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_BTN_PHONE = (By.ID, "t-btn-tab-phone")
    AUTH_BTN_EMAIL = (By.ID, "t-btn-tab-mail")
    AUTH_BTN_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_BTN_LS = (By.ID, "t-btn-tab-ls")
    AUTH_INPUT_USERNAME = (By.ID, "username")
    AUTH_INPUT_PASSWORD = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    FOGOT_PASS =(By.ID, "forgot_password")
    REGISTER = (By.ID, "kc-register")
    AUTH_USER_AGREEMENT = (By.XPATH, '//a[@href="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"]')
    AUTH_VK = (By.ID, "oidc_vk")
    AUTH_OK = (By.ID, "oidc_ok")
    AUTH_MAIL = (By.ID, "oidc_mail")
    AUTH_GOOGLE = (By.ID, "oidc_google")
    AUTH_YA = (By.ID, "oidc_ya")
    FOOTER_AGREEMENT = (By.ID, "rt-footer-agreement-link")



class RegLocators:
    REG_NAME = (By.ID, "firstName")
    REG_SURNAME = (By.ID, "lastName")
    REG_EMAIL_PHONE = (By.ID, "address")
    REG_PASSWORD = (By.ID, "password")
    REG_REPEAT_PASS = (By.ID, "password-confirm")
    REG_BTN = (By.NAME, "register")
    REG_USER_AGREEMENT = (By.XPATH, '//a[@href="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"]')


class RecovLocators:
    RECOV_BTN_PHONE = (By.ID, "t-btn-tab-phone")
    RECOV_BTN_EMAIL = (By.ID, "t-btn-tab-mail")
    RECOV_BTN_LOGIN = (By.ID, "t-btn-tab-login")
    RECOV_BTN_LS = (By.ID, "t-btn-tab-ls")
    RECOV_USERNAME = (By.ID, "username")
    RECOV_BTN = (By.ID,"reset")
    BACK_TO_AUTH = (By.ID, "reset-back")



