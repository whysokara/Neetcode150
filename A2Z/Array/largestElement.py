
## Using sorting

# def largestElement(nums):
#     nums.sort() ## O(nlogn)
#     return nums[-1]

def largestElement(nums):
    largest = float('-inf')
    for i in range(len(nums)): ## O(n)
        if nums[i] > largest:
            largest = nums[i]
    return largest


nums = [3,2,1,5,2]
print(largestElement(nums))