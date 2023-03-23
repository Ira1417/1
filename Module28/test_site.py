
from data import CURRECT_PASS, CURRECT_EMAIL
from pages import AuthPage, RegPage, RecovPage

import time



def test_reg_page_correct_reg(driver):
    page = RegPage(driver)
    page.enter_name("Тест")
    page.enter_surname("Тест")
    page.enter_email_phone("00@m.com")
    page.enter_pass("Test5222")
    page.enter_repeat_pass("Test5222")
    page.btn_click()
    time.sleep(3)

    assert page.driver.find_element_by_id('code - input - container').size != 0

    time.sleep(3)


def test_auth_page_correct_phone_and_pass(driver):
    page = AuthPage(driver)
    page.enter_username("89081187425")
    page.enter_pass(CURRECT_PASS)
    page.btn_click()


    assert page.driver.find_element_by_id('lk-btn').size != 0

    time.sleep(5)


def test_auth_page_correct_email_and_pass(driver):
    page = AuthPage(driver)
    page.btn_email_click()
    time.sleep(2)
    page.enter_username(CURRECT_EMAIL)
    page.enter_pass(CURRECT_PASS)
    page.btn_click()
    time.sleep(3)

    assert page.driver.find_element_by_id('lk-btn').size != 0
    time.sleep(5)


def test_auth_page_no_correct_login(driver):
     page = AuthPage(driver)
     page.btn_login_click()
     time.sleep(2)
     page.enter_username("000")
     page.enter_pass(CURRECT_PASS)
     page.btn_click()

     assert page.driver.find_element_by_id('form - error - message').size != 0

     time.sleep(5)


def test_auth_page_icon_vk(driver):
    page = AuthPage(driver)
    page.btn_vk_click()
    time.sleep(5)

   # assert page.driver.find_element_by_id("oauth_wrap_content").is_displayed()
    assert page.driver.find_element_by_id('oauth_wrap_content').size != 0
    time.sleep(2)


def test_auth_page_go_to_regpage(driver):
    page = AuthPage(driver)
    page.link_register_click()
    time.sleep(3)

    assert page.get_relative_link == "/registration"
    # assert page.url == RegPage
    time.sleep(2)


def test_auth_page_go_to_recovpage(driver):
    page = AuthPage(driver)
    page.link_fogot_pass_click()
    time.sleep(3)

    assert page.get_relative_link == "/reset-credentials"
   # assert page.url == RecovPage

    time.sleep(5)


def test_reg_page_name_tire(driver):
    page = RegPage(driver)
    page.enter_name("--")
    page.enter_surname("--")
    page.enter_email_phone(CURRECT_EMAIL)
    page.enter_pass(CURRECT_PASS)
    page.enter_repeat_pass(CURRECT_PASS)
    page.btn_click()


    assert page.driver.find_element_by_id('code - input - container').size != 0

    time.sleep(5)


def test_auth_page_footer_user_agreement(driver):
    page = AuthPage(driver)
    page.link_footer_user_agreement()
    time.sleep(3)


    assert page.url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
   # assert page.get_relative_link == "/agreement"

    time.sleep(5)


def test_auth_page_no_correct_ls(driver):
    page = AuthPage(driver)
    page.btn_ls_click()
    time.sleep(2)
    page.enter_username("000000000000")
    page.enter_pass(CURRECT_PASS)
    page.btn_click()

    assert page.driver.find_element_by_id("form - error - message") != 0

    time.sleep(5)


def test_reg_page_with_also_reg_email(driver):
    page = RegPage(driver)
    page.enter_name("Те")
    page.enter_surname("Те")
    page.enter_email_phone(CURRECT_EMAIL)
    page.enter_pass("Zz000000")
    page.enter_repeat_pass("Zz000000")
    page.btn_click()
    time.sleep(3)


    assert page.driver.find_element_by_id("reg-err-reset-pass") != 0

    time.sleep(5)


def test_recov_page_to_email_simbol_field_empty(driver):
    page = RecovPage(driver)
    page.btn_email_click()
    time.sleep(2)
    page.enter_username(CURRECT_EMAIL)
    page.btn_click()

    assert page.driver.find_element_by_id("form - error - message") != 0

    time.sleep(5)


def test_recov_page_link_go_back(driver):
    page = RecovPage(driver)
    page.link_back_to_auth_click()
    time.sleep(3)

    assert page.get_relative_link == "/authenticate"
   # assert page.url == AuthPage

    time.sleep(5)


def test_reg_page_user_agreement(driver):
    page = RegPage(driver)
    page.link_reg_user_agreement_click()
    time.sleep(2)

    assert page.url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"

    time.sleep(5)


def test_auth_page_icon_ya(driver):
    page = AuthPage(driver)
    page.btn_ya_click()
    time.sleep(3)


    assert page.driver.find_element_by_class_name("Authorize - card") != 0

    time.sleep(5)
