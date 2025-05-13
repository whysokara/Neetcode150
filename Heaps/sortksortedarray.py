import heapq

def nerlySortedArray(nums, k):
    min_heap = nums[:k + 1]
    heapq.heapify(min_heap)
    new_heap = []

    for num in range(k+1,len(nums)):
        new_heap.append(heapq.heappop(min_heap))
        heapq.heappush(min_heap, nums[num])

        # if len(min_heap) > k:
        #     heapq.heappush(new_heap, min_heap[0])

    while min_heap:
        new_heap.append(heapq.heappop(min_heap))
    return new_heap



nums = [6,5,3,2,8,10,9]
k = 3
print(nerlySortedArray(nums, k))