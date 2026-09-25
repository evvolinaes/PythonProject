#matrix = [
 #   [0, 0, 0],
   #  [0, 0, 0],
   #  [0, 0, 0],
  #  [0, 0, 0],
# ]

n=  int(input())
m = int(input())
matrix = []

#[0] * 3 -> [0, 0, 0]

for i in range(n):
    matrix.append([0] * m)

for row in matrix:
    print(*row)