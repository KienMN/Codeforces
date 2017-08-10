name = list(input())
name.insert(0, 'a')
n = len(name)
steps = 0
for i in range(1, n):
    distance = abs(ord(name[i]) - ord(name[i - 1]))
    steps += min(distance, 26 - distance)
print(steps)
