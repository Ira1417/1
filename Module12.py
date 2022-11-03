per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(per_cent.values())
money = input('Money = ')
m = int(money)
for index, item in enumerate(deposit):
   	if item > 1.0:
   		deposit[index] = (round((m * deposit[index] * 1) / 100));
print('deposit =', deposit)
max_number = max(deposit)
print('Максимальная сумма, которую вы можете заработать', max_number)
