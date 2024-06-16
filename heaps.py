

class MaxHeap:

    def __init__(self, arr=None):
        self.heap = []
        if type(arr) is list:
            self.heap = arr.copy()
            for i in range(len(self.heap))[::-1]:
                self._siftdown(i)

    def _siftup(self, i):
        parent = (i-2)//2
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i] 
            i = parent
            parent = (i-2)//2

    def _siftdown(self, i):
        left = i*2 + 1
        right = i*2 + 2
        while(left < len(self.heap) and self.heap[i] < self.heap[left] or right < len(self.heap) and self.heap[i]> self.heap[right]):
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i]
            i = biggest
            left = 2*i + 1
            right = 2*i + 2

    def insert(self, element):
        self.heap.append(element)
        self._siftup(len(self.heap)-1)

    #which is get_min for MinHeap
    def get_max(self): 
        return self.heap[0] if len(self.heap) > 0 else None
    
    #which is extract_min for MinHeap
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



