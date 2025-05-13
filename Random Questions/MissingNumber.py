def missingNumber(nums):
    ## brute force
    n = len(nums)
    # x1 = 0
    # x2 = 0

    # for i in range(n+1):
    #     x1 += i  ## can also use n*(n+1)//2

    # for j in nums:
    #     x2 += j

    # return x1-x2
    ans = 0
    for i in range(n+1):
        ans ^= i
    
    for num in nums:
        ans ^= num

    return ans




nums = [3,0,1]
print(missingNumber(nums))