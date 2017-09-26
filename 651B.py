n = int(input())
painting = [int(x) for x in input().split()]
nums = {}
appearance = {}
for i in range (n):
    if nums.get(painting[i]) == None:
        nums[painting[i]] = 1
    else:
        nums[painting[i]] += 1
for n in nums.keys():
    tmp = nums[n]
    while tmp > 0:
        if appearance.get(tmp) == None:
            appearance[tmp] = 1
        else:
            appearance[tmp] += 1
        tmp -= 1
res = 0
for a in appearance.keys():
    res += appearance[a] - 1
print(res)
