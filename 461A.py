n = int(input())
value = []
set = [int(x) for x in input().split()]
maxElement = max(set)
sumSet = sum(set)
total = sumSet
for i in range (0, maxElement + 1):
    value.append(0)
for i in range (0, n):
    value[set[i]] += 1
for i in range (0, maxElement + 1):
    while value[i] != 0:
        total += sumSet
        sumSet -= i
        value[i] -= 1

print(total - maxElement)
