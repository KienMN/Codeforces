n, k = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]
maxElement = max(times)
tmp = []
label = []
for x in times:
    tmp.append(x)
for i in range (0, maxElement + 1):
    label.append(0)
tmp.sort()
total = tmp[0]
numOfIns = 0
while total <= k:
    label[tmp[numOfIns]] += 1
    numOfIns += 1
    if numOfIns == n:
        break
    total += tmp[numOfIns]

print(numOfIns)
for i in range (0, n):
    if label[times[i]] != 0:
        print(i + 1, end=" ")
        label[times[i]] -= 1
