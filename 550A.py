string = list(input())
n = len(string)
i = 0
checkAB = []
checkBA = []
while i < n - 1:
    if string[i] == 'A' and string[i + 1] == 'B':
        checkAB.append([i, i + 1])
    elif string[i] == 'B' and string[i + 1] == 'A':
        checkBA.append([i, i + 1])
    i += 1
check = False
for x in checkAB:
    for y in checkBA:
        if x[0] not in y and x[1] not in y:
            check = True
            break
if check:
    print("YES")
else:
    print("NO")
