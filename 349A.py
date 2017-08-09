n = int(input())
check = True
money = [int(x) for x in input().split()]
note = {25: 0, 50: 0, 100: 0}
for m in money:
    if m == 25:
        note[25] += 1
    elif m == 50:
        if note[25] > 0:
            note[50] += 1
            note[25] -= 1
        else:
            check = False
            break
    elif m == 100:
        note[100] += 1
        if note[25] > 0 and note[50] > 0:
            note[25] -= 1
            note[50] -= 1
        elif note[25] > 2:
            note[25] -= 3
        else:
            check = False
            break


if check:
    print("YES")
else:
    print("NO")
