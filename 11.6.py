numbers = [8, 9, 10, 11]

numbers[1] = 17
numbers.extend([4,5,6])
del numbers[0]
numbers *= 2
n_copy = numbers.copy()
# numbers.extend(n_copy)
n_copy.insert(3,25)
# print(numbers)
print(n_copy)

