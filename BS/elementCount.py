def firstOccurance(arr,target):

    start = 0
    end = len(arr) -1
    res = -1
    while start <= end:
        #  mid = (start+end) // 2
         mid = start + (end - start) // 2
         if arr[mid] == target:
             res = mid
             end = mid - 1
         elif arr[mid] > target:
            end = mid - 1
         else:
            start = mid + 1
    return res

def lastOccurance(arr,target):

    start = 0
    end = len(arr) -1
    res = -1
    while start <= end:
        #  mid = (start+end) // 2
         mid = start + (end - start) // 2
         if arr[mid] == target:
             res = mid
             start = mid + 1
         elif arr[mid] > target:
            end = mid - 1
         else:
            start = mid + 1
    return res

arr = [3,4,10,10,10,10,12,12,13,15]
target = 10

first = firstOccurance(arr, target)
last = lastOccurance(arr, target)

## check if element doesn't exsists

if first == -1:
    print(-1)
else:
    print(last - first + 1)