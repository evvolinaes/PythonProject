n = int(input())
summa = 0
i = n
while i >= 0:
    if i % 2 == 0:
        summa = summa + i
    i = i-1
print(summa)