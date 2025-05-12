## brute force
# def kthsmallest(arr, k):
#     arr.sort()

#     return arr[k-1]

## using heap
import heapq
def kthsmallest(nums, k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return -max_heap[0]
        
        


nums = [2,1,5,6,4]
k = 3
print(kthsmallest(nums, k))