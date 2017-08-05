import math

n = int(input())
checkPrime = []
numbers = [int(x) for x in input().split()]

for i in range (0, 1000000 + 1):
    checkPrime.append(1)
checkPrime[0] = 0
checkPrime[1] = 0
for i in range (2, 1000 + 1):
    if (checkPrime[i] == 1):
        for j in range (i + i, 1000000 + 1, i):
            checkPrime[j] = 0

for number in numbers:
    check = True
    sqrt = int(math.sqrt(number))
    if sqrt ** 2 != number:
        check = False
    if check and checkPrime[sqrt] == 1:
        print("YES")
    else:
        print("NO")
