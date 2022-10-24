per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money    = int(input("Введите сумму, которую планируете положить под проценты: "))
deposit  = list()

for percent in per_cent.values():
    deposit.append(int(money / 100 * percent))

print(f"Максимальная сумма, которую вы можете заработать — {max(deposit)}")
