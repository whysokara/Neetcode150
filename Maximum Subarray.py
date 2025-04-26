## Brute Force
class Solution:
    def maxSubArray(self, nums):
        ans = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans

## Kadane's Algorithm
arr = [-2,1,-3,4,-1,2,1,-5,4]
maxSub = arr[0]
curSum = 0

for i in arr:
    if curSum < 0:
        curSum = 0
    curSum += i
    maxSub = max(maxSub, curSum)

print(maxSub)
