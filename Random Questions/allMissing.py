def allMissingNumber(nums):
    n = len(nums)

    ## brute force
    # ans = []
    # seen = set(nums)

    # for i in range(1, n+1):
    #     if i not in seen:
    #         ans.append(i)

    # return ans

    




nums = [4,3,2,7,8,2,3,1]
print(allMissingNumber(nums))