n, k = [int(x) for x in input().split()]
passwords = []
maxTime = 1
minTime = 1
for i in range (n):
  passwords.append(str(input()))
truePassword = str(input())
for i in range (n):
  if len(passwords[i]) < len(truePassword):
    maxTime += 1
    minTime += 1
  elif len(passwords[i]) == len(truePassword) and passwords[i] != truePassword:
    maxTime += 1
res1 = int(minTime / k) * 5 + minTime
res2 = int(maxTime / k) * 5 + maxTime
if minTime % k == 0:
  res1 -= 5
if maxTime % k == 0:
  res2 -= 5
print(res1, res2)
