import heapq

def ksmallest(nums, k):
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [-x for x in max_heap]

nums = [3,4,7,10,15,20]
k = 3

print(ksmallest(nums, k))
