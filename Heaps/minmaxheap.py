## min heap
import heapq

pq = []

heapq.heappush(pq, 3)
heapq.heappush(pq, 4)
heapq.heappush(pq, 2)
smallest = pq[0]

print(smallest)