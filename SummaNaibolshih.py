numbers = list(map(int, input().split()))


numbers.sort(reverse=True)
#print(numbers)
#summa = numbers[-1] +numbers[-2] + numbers[-3]

print(sum(numbers[-3:]))

