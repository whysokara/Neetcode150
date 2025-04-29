def agnosticBinarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    isAscending = arr[start] < arr[end]  # Check order only once

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid

        if isAscending:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1

# Ascending array
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(agnosticBinarySearch(arr1, 9))  # Output: 8

# Descending array
arr2 = [100, 90, 80, 70, 60, 50, 40]
print(agnosticBinarySearch(arr2, 70))  # Output: 3
