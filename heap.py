class Heap:
    """
    implements a min heap in an array
    """

    _heap = []

    def findMin(self):
        return self._heap[0]

    def removeMin(self):
        elem = self._heap.pop()
        self._heap[0] = elem
        self.downHeap(1)

    def insert(self, elem):
        self._heap.append(elem)
        child = len(self._heap)
        self.upheap(child)

    def downHeap(self, parent):
        if (parent * 2 >= len(self._heap)):
            return

        parentIdx = parent - 1
        child1Idx = parent * 2 - 1
        child2Idx = parent * 2
        if (self._heap[child1Idx] <= self._heap[child2Idx]):
            childIdx = child1Idx
        else:
            childIdx = child2Idx

        if (self._heap[parentIdx] > self._heap[childIdx]):
            self._heap[parentIdx], self._heap[childIdx] = self._heap[childIdx], self._heap[parentIdx]
            self.downHeap(childIdx + 1)

    def upheap(self, child):
        if (child == 1):
            return

        if child % 2 == 1:
            parent = ((child - 1) / 2)
        else:
            parent = child / 2

        childIdx = child - 1
        parentIdx = parent - 1
        if self._heap[parentIdx] <= self._heap[childIdx]:
            return
        else:
            self._heap[parentIdx], self._heap[childIdx] = self._heap[childIdx], self._heap[parentIdx]
            self.upheap(parent)

h = Heap()
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(4)
h.insert(5)
h.removeMin()
h.insert(1)
print(h._heap)
