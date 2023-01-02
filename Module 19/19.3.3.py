import requests
import json

status = 'sold'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
print(res.json())


data = {'name':"Бегемот"}
res = requests.post(f'https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json'}, json=data)
print(res.json())


data = {'id':'9223372036854587608', 'name':"Матрос"}
res = requests.put(f"https://petstore.swagger.io/v2/pet", json=data)
print(res.json())

dict = json.dumps(res.json())
dict1 = json.loads(dict)
print(dict1)
pet = dict1.get('id')
print(pet)
pet_id = pet
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers={'accept':'application/json'})


print(res.json())
