# ## using set
# def removeDuplicates(nums):
#     return list(set(nums))

def removeDuplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i+=1
    return nums[:i+1]


nums = [1,1,2,2,2,3,3]
print(removeDuplicates(nums))