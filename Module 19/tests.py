from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_false_password(email=valid_email, password=false_password):
    """ Проверяем что запрос api ключа при введении неверного пароля возвращает статус не равный 200 и в результате не содержится слово key"""

    false_password = '2414f5'
    status, result = pf.get_api_key(email, false_password)
    
    assert status != 200
    assert 'key' not in result

def test_add_new_pet_with_valid_data_whiout_photo(name='Бегемот', animal_type='магическией кот',
                                     age='100'):
     """Проверяем что можно добавить питомца с корректными данными без фото"""

     # Запрашиваем ключ api и сохраняем в переменую auth_key
     _, auth_key = pf.get_api_key(valid_email, valid_password)

     # Добавляем питомца
     status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

     # Сверяем полученный ответ с ожидаемым результатом
     assert status == 200
     assert result['name'] == name


def test_successful_add_pet_foto(pet_photo='image/12.jpg'):
    """Проверяем возможность добавление фото питомца"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pet")

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo='image/12.jpg')

    assert status == 200
    assert result['pet_photo'] == pet_photo



def test_add_new_pet_with_empty_data_whiout_photo(name='', animal_type='',
                                                  age=''):
    """Проверяем что можно добавить питомца с пустыми данными без фото"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert len(result['name']) == 0

def test_update_self_pet_info_only_name_with_nothing_else(name='Мататаби', animal_type='', age=''):
    """Проверяем что если при обновлении информации о питомце указать только имя, то остальные данные останутся прежними"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name and len(result['animal_type']) != 0 and len(result['age']) != 0
        print(name)
    else:
        raise Exception("There is no my pets")


def test_add_new_pet_with_false_format_age_(name='Шарик', animal_type='пес',
                                                  age='dfbj'):
    """Проверяем можно ли указать возраст животного не в цифрах, а словами"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result
    """"Здась баг, потому что сайт должен принимать возраст только в формате числа(int), а не в любом(str)"""

def test_delete_self_pet_with_false_pet_id():
    """Проверяем, что при удалении питомца с пустым id программа выдает ошибку"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Берём пустой id и отправляем запрос на удаление
    pet_id = ''
    status, _ = pf.delete_pet(auth_key, pet_id)

    assert status != 200

def test_get_all_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос списка моих питомцев по filter 'my_pets' возвращает спиок моих
    питомцев и проверяем, что список не пустой"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0
    print(result)

