n = int(input())
store = []

prices = [int(x) for x in input().split()]
maxPrice = max(prices)
for i in range(0, maxPrice + 1):
    store.append(0)
for x in prices:
    store[x] += 1
for i in range(1, maxPrice + 1):
    store[i] += store[i - 1]

q = int(input())
for i in range (0, q):
    m = int(input())
    if m >= maxPrice:
        print(n)
    else:
        print(store[m])
