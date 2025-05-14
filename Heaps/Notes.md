## Heap
* if a node is at index i, then
* left child is at 2*i
* right child is at 2*1+1
* parent child is at i// (floor)

### Identify HEAP questions
* will have K in question
* will have smallest/largest in question

> if asked kth smallest then create max heap and vice versa

> Min heap 
``` python
import heapq

pq = []
heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 5)
smallest = pq[0]
```
> Max heap
``` python
import heapq

pq = []
heapq.heappush(pq, -3)
heapq.heappush(pq, -1)
heapq.heappush(pq, -5)
largest = -pq[0]

```