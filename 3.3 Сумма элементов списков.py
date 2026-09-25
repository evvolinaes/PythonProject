numbers1 = list(map(int, input().split()))#[3, 5, -2, 0, 12]
numbers2 = list(map(int, input().split())) #[1, -5, 4, 8, 8]
total = []

#ка кпройтись по индексам
for index in range(len(numbers1)):
    #range(len(numbers1)) возьми размер списка каким бы они ни был или сгенерируй каким бы ни был длиной
    summa = numbers1[index] + numbers2[index]
    total.append(summa)

print(total)