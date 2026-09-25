numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
total = []

for el1, el2 in zip(numbers1, numbers2):
    total.append(el1+el2)