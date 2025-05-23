import heapq

def klargest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap

nums = [3,4,7,10,15,20]
k = 3

print(klargest(nums, k))
