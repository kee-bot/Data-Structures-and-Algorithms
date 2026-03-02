class MinHeap:
    def __init__(self):
        self.heap = []

    # ---------- Helper Index Methods ----------
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # ---------- Swap ----------
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # ---------- Insert ----------
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    # ---------- Extract Min ----------
    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self._heapify_down(smallest)

    # ---------- Peek ----------
    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    # ---------- Size ----------
    def size(self):
        return len(self.heap)

    # ---------- Build Heap from List ----------
    def heapify(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(8)
    min_heap.insert(1)

    print("Min Heap:", min_heap.heap)  # Min Heap: [1, 3, 8, 5]
    print("Extracted Min:", min_heap.extract_min())  # Extracted Min: 1
    print("Min Heap after extraction:", min_heap.heap)  # Min Heap after extraction: [3, 5, 8]
    print("Peek Min:", min_heap.peek())  # Peek Min: 3
    print("Size of Heap:", min_heap.size())  # Size of Heap: 3

    # Building heap from a list
    arr = [7, 2, 6, 4, 9]
    min_heap.heapify(arr)
    print("Min Heap from list:", min_heap.heap)  # Min Heap from list: [2, 4, 6, 7, 9]