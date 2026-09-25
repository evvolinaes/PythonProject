# 1.Ввод данных
#2.Вывести все числа от 0...n
#3.Вывести только четные
#4.найти сумму

n = int(input())
i=0
summa = 0
while i<=n:
    n=n+1
    if n%2==0:
        summa = summa+n
    print(summa)