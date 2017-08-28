n, t = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]
books = []
for i in range (n):
  books.append(0)
currentTime = 0
if times[n - 1] <= t:
  currentTime += times[n - 1]
  books[n - 1] += 1
for i in range (n - 2, -1, -1):
  if currentTime + times[i] <= t:
    currentTime += times[i]
    books[i] = books[i + 1] + 1
  else:
    j = books[i + 1]
    while j > 0:
      currentTime -= times[i + j]
      if currentTime + times[i] <= t:
        currentTime += times[i]
        break
      j -= 1
    books[i] = j
print(max(books))
