numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))

for el1, el2 in zip(numbers1, numbers2):
    print(el1, el2)