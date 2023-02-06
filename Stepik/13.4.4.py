# объявление функции
def merge(list1, list2):
    for el in range(len(list2)):
        list1.append(list2[el])
    list1.sort()
    return list1

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]


# вызываем функцию
print(merge(numbers1, numbers2))