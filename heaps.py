

class MaxHeap:

    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-1)//2
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i] 
            i = parent
            parent = (i-2)//2



    def _siftdown(self, i):
        left = i*2 + 1
        right = i*2 + 2
        while(left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i]> self.heap[right]):
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            i = biggest
            left = 2*i + 1
            right = 2*i + 2
  


    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_max(self): 
        return self.heap[0] if len(self.heap) > 0 else None
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return max_val
    
    def update_index_val(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new > old:
            self._siftup(i)
        else:
            self._siftdown(i)




class MinHeap:

    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)


    def _siftup(self, i):
        parent = (i-2)//2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i] 
            i = parent
            parent = (i-2)//2


    def _siftdown(self, i):
        left = i*2 + 1
        right = i*2 + 2
        while(left < len(self.heap) and self.heap[i] > self.heap[left]) or (right < len(self.heap) and self.heap[i] > self.heap[right]):
            smallest = left if (right >= len(self.heap) or self.heap[left] < self.heap[right]) else right
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
            left = 2*i + 1
            right = 2*i + 2


    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    def get_min(self): 
        return self.heap[0] if len(self.heap) > 0 else None
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._siftdown(0)
        return min_val
    
    def update_index_val(self, i, new):
        old = self.heap[i]
        self.heap[i] = new
        if new > old:
            self._siftup(i)
        else:
            self._siftdown(i)
            


def heapsort(arr):
    heap = MinHeap(arr)
    sorted_arr = [heap.extract_min() for i in range(len(heap.heap))]

    return sorted_arr


class PriorityQueue:

    def __init__(self):
        self.queue = MaxHeap()

    def enqueue(self, element):
        self.queue.insert(element)
    
    def peek(self):
        return self.queue.get_max()
    
    def dequeue(self):
        return self.queue.extract_max()
    
    def change_priority(self, i, new):
        self.queue.update_index_val(i, new)

    def is_empty(self):
        return len(self.queue.heap) == 0


arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]



print(arr)
print('sorted array: ' ,heapsort(arr))


q = PriorityQueue()

print('\nis the queue empty:' , q.is_empty())

for i in arr[:5]:
    q.enqueue(i)
    
print('queue:', q.queue.heap)

q.dequeue()

print('queue after one dequeue:', q.queue.heap)

print('the heighest priority queue', q.peek())

q.change_priority(2, 20)

print('queue after priority change:', q.queue.heap)
print('\nis the queue empty:' , q.is_empty())
