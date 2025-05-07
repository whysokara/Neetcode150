def leftRotate(nums):
    for i in range(len(nums)):
        nums[i] = nums[len(nums)-1]
    return nums
nums = [1,2,3,4,5]
print(leftRotate(nums))