n = int(input())
countRating = []
sequence = []
for i in range (0, 2001):
    countRating.append(0)
    sequence.append(0)

rating = [int(x) for x in input().split()]

for rate in rating:
    countRating[rate] += 1

for i in range (2000, 0, -1):
    if countRating[i] != 0:
        sequence[i] = 1
        for j in range (i - 1, 0, -1):
            sequence[j] = sequence[j + 1] + countRating[j + 1]
        break

for rate in rating:
    print(sequence[rate], end=" ")