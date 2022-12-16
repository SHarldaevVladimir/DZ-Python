# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
#  Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


from math import sqrt

# P = a*b       a = P/b    P/b = S-b      p = Sb -  bb   b^2-Sb+P=0  D = s^2-4P
# S = a+b       a = S-b
def calculate(b, c):
    D = b*b - 4*c  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        x1 = b/2-sqrt(D)/2
        x2 = b/2+sqrt(D)/2
    return [x1, x2]

def main():
    b = int(input('Enter sum: '))
    c = int(input('Enter mul: '))
    print(calculate(b, c))

main()