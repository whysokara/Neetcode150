def secondSmallest(nums):
    smallest = secondSmallest = float('inf')
    for i in range(len(nums)):
        if nums[i] < smallest:
            secondSmallest = smallest
            smallest = nums[i]
        elif secondSmallest > nums[i] > smallest:
            secondSmallest = nums[i]

    return secondSmallest if secondSmallest != float('inf') else None


nums = [3,1,4,5,3,3,9]
print(secondSmallest(nums))