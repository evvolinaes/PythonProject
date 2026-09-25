n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for index in range(len(matrix)):
    print(matrix[index][index])

for row in matrix:
    print(*row)