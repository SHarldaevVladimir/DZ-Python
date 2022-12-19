# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве.
# и число, которое необходимо проверить - X.

# 5
# 1 2 0 4 7
# 6

# -> 7

import random
import os
os.system('cls')

print(" Задача 18:")
print("Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.")
print("Пользователь вводит натуральное число N – количество элементов в массиве.")
print("и число, которое необходимо проверить - X.")
print()
n = int(input("Введите число N: "))
l = []
for num in range(0, n):
    random_number = round(random.randint(0, 10))
    l.append(random_number)

print(l)
x = int(input("Введите число X: "))


def checkNumber(count):

    for i in range(0, len(l)):
        if l[i] == x+count:
            return l[i]
        elif l[i] == x-count:
            return l[i]

    return checkNumber(count+1)


print(checkNumber(0))

# print()
# print("Второй способ: ")
# m = int(input("Введите число N: "))
# a = []
# for num in range(0, m):
#     random_number = round(random.randint(0, 10))
#     a.append(random_number)

# print(a)
# b = int(input("Введите число X: "))
# number=0
# for i in range(len(a)):
#     if (b-a[i])<b-number and b-a[i]>0:
#         number=i
# print(a[number])

