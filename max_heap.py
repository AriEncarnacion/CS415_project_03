class MaxHeap:

    def __init__(self, ratios):
        self.heap = [*[-1], *ratios]  # add -1 to front of heap to simplify integer division
        self.n = len(self.heap) - 1
        self.operations = 0

    def build_heap(self):
        if self.n <= 1:
            return
        rmp = self.n // 2
        while rmp > 0:
            self.sift_down(rmp)
            rmp -= 1

    def sift_down(self, pt):
        while pt <= self.n // 2:
            if pt*2+1 > self.n:
                self.swap(pt, pt*2)
                return
            elif self.heap[pt*2] >= self.heap[pt*2+1]:
                self.swap(pt, pt*2)
                pt = pt*2
            else:
                self.swap(pt, pt*2+1)
                pt = pt*2+1
            self.operations += 1                        # +1 comparison, greater of both child values

    def swap(self, pt, cd):
        self.operations += 1                            # +1 comparison, is parent > child
        if self.heap[pt] < self.heap[cd]:
            self.heap[pt], self.heap[cd] = self.heap[cd], self.heap[pt]

    def delete_max(self):
        if self.n == 0:
            return -1
        m = self.heap[1]
        self.heap[1], self.heap[self.n] = self.heap[self.n], self.heap[1]
        self.n -= 1
        self.sift_down(1)
        return m

    def get_operations(self):
        return self.operations

    def get_heap(self):
        return self.heap

