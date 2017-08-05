n = int(input())
location = [int(x) for x in input().split()]
for i in range(0, n):
    if location[i] == location[0]:
        mi = location[i + 1] - location[i]
        ma = location[n - 1] - location[i]
    elif location[i] == location[n - 1]:
        mi = location[i] - location[n - 2]
        ma = location[i] - location[0]
    else:
        min1 = abs(location[i] - location[i - 1])
        min2 = abs(location[i] - location[i + 1])
        mi = min(min1, min2)
        max1 = abs(location[i] - location[0])
        max2 = abs(location[i] - location[n - 1])
        ma = max(max1, max2)
    print(mi, ma)