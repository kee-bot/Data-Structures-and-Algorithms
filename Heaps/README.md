# Heaps

A heap is a specialized tree-based data structure that satisfies the heap property:

- In a min-heap the parent is always <= its children (root is the minimum element).
- In a max-heap the parent is always >= its children (root is the maximum element).

```mermaid
graph TB
	 A[10] --> B[15]
	 A --> C[30]
	 B --> D[40]
	 B --> E[50]
	 C --> F[100]
```

Most questions regarding heaps follow a similar pattern (extract-min/extract-max, push, build-heap, replace).  

Python has the below heapq functions which are useful while solving heap problems.

1. heapq.heappop(heap)

	- Description: Remove and return the smallest item from the heap.
	- Complexity: O(log n) because the heap must be rebalanced after removal.

	Example:

	```python
	import heapq

	heap = [1, 3, 5]
	heapq.heapify(heap)  # ensure it's a heap
	smallest = heapq.heappop(heap)  # returns 1
	```

2. heapq.heappush(heap, item)

	- Description: Push a new item onto the heap, maintaining the heap invariant.
	- Complexity: O(log n).

	Example:

	```python
	heapq.heappush(heap, 2)  # heap now contains 2 as appropriate position
	```

3. heapq.heapify(x)

	- Description: Transform list `x` into a heap, in-place.
	- Complexity: O(n)

	Example:

	```python
	data = [5, 3, 8, 1, 2]
	heapq.heapify(data)  # data is now a valid min-heap
	```

4. heapq.heappushpop(heap, item)

	- Description: Push `item` on the heap then pop and return the smallest item. More efficient than `heappush()` followed by `heappop()` because it only balances the heap once.
	- Complexity: O(log n)

	Example:

	```python
	val = heapq.heappushpop(heap, 4)
	# pushes 4 and pops the smallest element in one operation
	```

## Implementations

1. [Implementation.py](Implementation.py) Implementation of heap operations

## Practice Exercises

1. [01_kth_largest.py](practice_exercises/01_kth_largest.py) - Practice: Find the k-th largest element using a heap.
2. [02_k_closest.py](practice_exercises/02_k_closest.py) - Practice: Find k closest points to the origin (use heap for top-k).
3. [03_k_freq.py](practice_exercises/03_k_freq.py) - Practice: Top-k frequent elements (use heap of frequencies).
4. [04_task_scheduler.py](practice_exercises/04_task_scheduler.py) - Practice: Task scheduler / cooldown problems (priority queue pattern).

## References

1. https://www.youtube.com/watch?v=lvO88XxNAzs
