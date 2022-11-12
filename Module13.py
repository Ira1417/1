bilet = int(input('Укажите количество билетов '))
num = input('Укажите возраст каждого посетителя ').split()
num_1 = list(map(int, num))
price = []
for i in num_1:
    if i < 18:
        price.append(0)
    elif 18 <= i < 25:
        price.append(990)
    else:
        price.append(1390)
if bilet >= 3 and len(num_1) >= 3:
    final_price = sum(price) - (sum(price) * 10) / 100
else:
    final_price = sum(price)
print('Цена билетов', int(final_price))
