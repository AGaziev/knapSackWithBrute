itemCount = 4
backPackSize = 5
items = [[1, 2], [2, 3], [3, 4], [4, 4]]
bestScore = {'kit': [], 'weight': 0, 'cost': 0}


def toBin(a, size):  # для определения
    a = bin(a)[2:]
    a = '0' * (size - len(a)) + a
    return a


for i in range(1, 2 ** itemCount):
    setOfItems = list(toBin(i, itemCount))  # инициализируем наборы (1 - берем, 0 - не берем)
    cost = 0  # стоимость взятых предметов
    weight = 0  # вес взятых предметов
    badFlag = False  # флаг переполнения рюкзака
    for index, state in enumerate(setOfItems):
        if state == '1':
            cost += items[index][1]     # Если есть в наборе то добавляем в стоимость
            weight += items[index][0]   # и вес
            if weight > backPackSize:  # если переполнен, то ставим флаг
                badFlag = True
                break
    print(setOfItems, cost, badFlag)
    if not badFlag:
        if bestScore['cost'] < cost:  # если найден лучший вариант меняем значения
            bestScore.update({'kit': [setOfItems], 'cost': cost})
        elif bestScore['cost'] == cost:  # если найден идентичный нужному, добавляем набор
            bestScore['kit'].append(setOfItems)

print(bestScore)
