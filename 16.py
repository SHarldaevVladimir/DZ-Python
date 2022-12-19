# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве.
# и число, которое необходимо проверить - X.

# 5
# 1 2 3 4 5
# 3
# -> 1

import os
os.system('cls')


import random

n = int(input("Введите число n: "))
x = int(input("Введите число x: "))
l = []
for num in range(0,n):
    random_number = round(random.randint(0,1))
    l.append(random_number)

print(l)

count = 0

for i in range(0, len(l)):
    if l[i] == x:
        count += 1

print(count)