arr = [-2,1,-3,4,-1,2,1,-5,4]
maxSub = arr[0]
curSum = 0

for i in arr:
    if curSum < 0:
        curSum = 0
    curSum += i
    maxSub = max(maxSub, curSum)

print(maxSub)
