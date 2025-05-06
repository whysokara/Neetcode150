
# brute
# def secondLargest(nums):
#     nums.sort() # O(nlogn)
#     largest = nums[-1]
#     second = float('-inf')
#     for i in range(len(nums)-1, -1,-1): # O(n)
#         if nums[i] != largest:
#             second = nums[i]
#             break;

#     return second # n+nlogn

# optimal

# def secondLargest(nums):
#     largest = float('-inf')
#     secondLargest = float('-inf')
#     for i in range(len(nums)):
#         if nums[i] > largest:
#             largest = nums[i]

#     for j in range(len(nums)):
#         if nums[j] > secondLargest and nums[j] != largest:
#             secondLargest = nums[j]

#     return secondLargest

def secondLargest(nums):
    largest = secondLargest = float('-inf')
    
    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif largest > num > secondLargest:
            secondLargest = num

    return secondLargest if secondLargest != float('-inf') else None

                    
nums = [1,6,2,4,7,7,5]
print(secondLargest(nums))