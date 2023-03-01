
import pytest

def test_show_my_pets():

   # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('isa87@mail.ru')
   # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('fas45x')
   # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя

    pytest.driver.implicitly_wait(5)
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    pytest.driver.implicitly_wait(5)
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    pytest.driver.implicitly_wait(5)
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ', ' in descriptions[i]
       parts = descriptions[i].text.split(", ")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0
