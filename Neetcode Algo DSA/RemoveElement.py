def removeElement(arr, value):
    j = 0

    for i in range(len(arr)):
        if arr[i] != value:
            arr[j] = arr[i]
            j += 1
    return j
arr = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(arr,2))
