n = int(input())
days = [int(x) for x in input().split()]
up = True
if n == 1:
    if days[0] == 0:
        print("UP")
    elif days[0] == 15:
        print("DOWN")
    else:
        print(-1)
else:

    yesterday = days[0]
    for i in range (1, n):
        today = days[i]
        if today > yesterday:
            up = True
        else:
            up = False
        if today == 15 or today == 0:
            up = not up
        yesterday = today
    if up:
        print("UP")
    else:
        print("DOWN")
