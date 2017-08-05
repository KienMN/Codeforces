def dec_to_bin(x):
    return bin(x)[2:]

def compare(x, y):
    charX = list(dec_to_bin(x))
    charY = list(dec_to_bin(y))
    differ = 0
    while (len(charX) < len(charY)):
        charX.insert(0, '0')
    while (len(charY) < len(charX)):
        charY.insert(0, '0')
    for i in range(0, len(charX)):
        if charX[i] != charY[i]:
            differ += 1
    print(charX)
    print(charY)
    print(differ)
    return differ

n, m, k = [int(x) for x in input().split()]
numbers = []
for i in range (0, m + 1):
    numbers.append(int(input()))
res = 0
for i in range(0, m):
    if compare(numbers[i], numbers[m]) <= k:
        res += 1
print(res)



# import math
# def isTPrime(x):
#     if x < 4:
#         return False
#     else:
#         divisor = 0
#         bound = int(math.sqrt(x)) + 1
#         for i in range(1, bound):

