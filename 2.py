# найти сумму цифр трехзначного числа

Number = int(input('Введите трехзначнчое число: '))
if Number<100 and Number>999: print ("Это не трехзначное: ")
else: 
    a = Number%10
    b = (Number//10)%10
    c = Number//100
    print('Сумма цифра числа равна:',a+b+c)

