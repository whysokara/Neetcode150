def binarySearchReverse(arr,target):

    start = 0
    end = len(arr) -1

    while start <= end:
        #  mid = (start+end) // 2
         mid = start + (end - start) // 2
         if arr[mid] == target:
             return (mid)
         elif arr[mid] > target:
            start = mid + 1
         else:
            end = mid - 1
    return -1

arr = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
target = 12

print(binarySearchReverse(arr, target))