def twoSum(nums, target):
    hash = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in hash:
            return [hash[diff],i]
        hash[n] = i




nums = [4,1,6,5,3]
target = 8
print(twoSum(nums, target))