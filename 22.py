# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

import random
n = int(input("Количестов элемнетов первого набора: "))
m = int(input("Количестов элемнетов второго набора: "))

array = []
for item in range(0,n):
    random_number = round(random.randint(0, 10))
    array.append(random_number)
data = []
for item in range(0,m):
    random_number = round(random.randint(0, 10))
    data.append(random_number)
numbers = {}
for item in array:
    if item in data:
        numbers[item] = item
    

print(array)
print(data)
print(set(numbers))

