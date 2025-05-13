def containsDuplicate(nums):
    n = len(nums)
# ## brute force
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] == nums[j]:
#                 return True
            
#     return False

## better
    # return len(nums) != len(set(nums))

## Best using set
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


nums = [1,2,3,1]
print(containsDuplicate(nums))