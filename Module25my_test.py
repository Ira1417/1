import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()

def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")
#
    time.sleep(3)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element_by_xpath("//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element_by_link_text(u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("isa87@mail.ru")

    # add password
    field_pass = web_browser.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("fas45x")

    # click submit button
    btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

    time.sleep(3)

    btn_exist_acc = web_browser.find_element_by_link_text('Мои питомцы')
    btn_exist_acc.click()


    pets = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody tr')))
    my_animals = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.task2 fill .col-sm-4 left text')))
    images = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')))
    names = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
    animal_type = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')))
    age = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')))
    all_names = []
    have_image = []


    for i in names:
        all_names.append(i.text)


    for i in range(len(my_animals)):
        number = my_animals.text.split('/n')
        number_vse = number[1].split(' ')
        my_ani = int(number_vse[1])

        assert my_ani == len(pets)
        assert names[i].text != ''
        assert animal_type[i].text != ''
        assert age[i].text != ''

    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            have_image.append(1)

    assert len(have_image) >= len(pets) / 2
    assert len(list(set(all_names))) == len(pets)

    driver.quit()
