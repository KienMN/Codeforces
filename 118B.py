n = int(input())
size = 2 * n + 1
matrix = []
for i in range (0, size):
    row = []
    for j in range (0, size):
        row.append(' ')
    matrix.append(row)


for i in range (0, n + 1):
    matrix[i][n] = i
    j = 0
    while i - j >= 0:
        matrix[i][n - j] = i - j
        matrix[i][n + j] = i - j
        j += 1

for i in range (n + 1, size):
    matrix[i] = matrix[size - 1 - i]

for i in range (0, size):
    for j in range (0, size):
        if j == size - 1:
            print(matrix[i][j])
            break
        elif isinstance(matrix[i][j], int) and matrix[i][j + 1] == ' ':
            print(matrix[i][j])
            break
        else:
            print(matrix[i][j], end=" ")
