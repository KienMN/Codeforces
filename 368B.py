n, m = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
value = []
for i in range (0, 100001):
    value.append(0)
distinctNumbers = []
for i in range (0, n + 2):
    distinctNumbers.append(0)

for i in range (n - 1, -1, -1):
    if value[numbers[i]] == 0:
        value[numbers[i]] += 1
        distinctNumbers[i + 1] = distinctNumbers[i + 2] + 1
    else:
        distinctNumbers[i + 1] = distinctNumbers[i + 2]
for i in range (0, m):
    x = int(input())
    print(distinctNumbers[x])
