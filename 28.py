# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    else:
        return a + sum(1, b - 1)    

def numberA():
    A = int(input('Введите первое число: '))
    if A < 0:    
        print('Некорректный ввод! Введите целые неотрицательные числа. ')
        return numberA()
    else:
        return A

def numberB():
    B = int(input('Введите второе число: '))
    if B < 0:    
        print('Некорректный ввод! Введите целые неотрицательные числа. ')
        return numberB()
    else:
        return B
 
A = numberA()
B = numberB()
# result = sum(A,B)
print(f'{A} + {B} = {sum(A, B)}')