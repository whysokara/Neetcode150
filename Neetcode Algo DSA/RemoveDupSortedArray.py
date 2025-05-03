# nums = [0,0,1,1,1,2,2,3,3,4]
# n = len(nums)
# res = []
# for i in range(n):
#     if nums[i] not in res:
#         res.append(nums[i])
    
# for i in range(len(res)):
#     nums[i] = res[i]

# print(len(res))

## Optimised
def remove(arr):
  j = 1
  for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
      arr[j] = arr[i]
      j += 1
  return j

arr = [0,0,1,1,1,2,2,3,3,4]
print(remove(arr))
