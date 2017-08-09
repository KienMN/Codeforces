dic = {}
n, m = [int(x) for x in input().split()]
for i in range (0, m):
    a, b = input().split()
    if (len(a) > len(b)):
        dic[a] = b
    else:
        dic[a] = a
lecture = input().split()
for word in lecture:
    print(dic[word], end=" ")
