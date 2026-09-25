numbers = input().split()
target = input()

for number in numbers[:]:
    if number == target:
        numbers.remove(target)
print(*numbers)

#если внутри цикла модифицируем список, то мы модифицировать должны не сам список а его копию
#нелья и не хорошо проходиться по списку и потом его же модифицировать

#пример через while
#while target in numbers:
#numbers.remove(target)