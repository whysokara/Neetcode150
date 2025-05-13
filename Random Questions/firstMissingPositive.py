def firstMissingPositive(nums):
    n = len(nums)
    # brute force
    # num_set = set(nums)
    # for i in range(1,n + 2):
    #     if i not in num_set:
    #         return i

    
    # Function to swap elements in the array
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    for i in range(n):
        while 0 < nums[i] <= n and nums[i] != nums[nums[i]-1]:
            swap(nums, i, nums[i]-1)

    for i in range(n):
        if nums[i] != i+1:
            return i+1
        
    return n+1




nums = [3,4,-1,1]
print(firstMissingPositive(nums))