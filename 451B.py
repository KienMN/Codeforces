n = int(input())
a = [int(x) for x in input().split()]

fault = 0
currentMaxIncrease = 0
currentMinDecrease = 0
currentValue = 0
increase = True
check = False

for i in range (0, n):
    if fault <= 1:
        if increase:
            if a[i] < currentValue:
                fault += 1
                increase = not increase
                currentMinDecrease = i
            else:
                currentMaxIncrease = i
            currentValue = a[i]
        else:
            if a[i] > currentValue:
                increase = not increase
                fault += 1
            else:
                currentMinDecrease = i
            currentValue = a[i]
    else:
        if increase:
            if a[i] < currentValue:
                fault += 1
                increase = not increase
            currentValue = a[i]
        else:
            if a[i] > currentValue:
                increase = not increase
                fault += 1
            currentValue = a[i]

if fault == 0:
    print("yes")
    print(1, 1)
elif fault <= 2:
    if currentMaxIncrease != 0:
        if a[currentMinDecrease] > a[currentMaxIncrease - 1]:
            check = True
    else:
        check = True
    if check:
        if currentMinDecrease != n - 1:
            if a[currentMaxIncrease] < a[currentMinDecrease + 1]:
                check = True
            else:
                check = False

    if check:
        print("yes")
        print(currentMaxIncrease + 1, currentMinDecrease + 1)
    else:
        print("no")
else:
    print("no")
