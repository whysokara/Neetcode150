def singleNumber2(nums):
    res = 0

    for num in nums:
        res ^= num
    return res

nums = [1,3,4,3,5,2,7,4,2,1,5]
print(singleNumber2(nums))