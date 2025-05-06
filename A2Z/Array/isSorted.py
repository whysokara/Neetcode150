def isSorted(nums):
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            return False
    return True

nums = [1,4,7,5,6,7,8]
print(isSorted(nums))