class MaxHeap:

    def __init__(self, ratios):
        self.max_heap = [*[-1], *ratios]  # add -1 to front of heap to simplify integer division
        self.n = len(self.max_heap) - 1
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
            elif self.max_heap[pt * 2] >= self.max_heap[pt * 2 + 1]:
                self.swap(pt, pt*2)
                pt = pt*2
            else:
                self.swap(pt, pt*2+1)
                pt = pt*2+1
            self.operations += 1                        # +1 comparison, greater of both child values

    def swap(self, pt, cd):
        self.operations += 1                            # +1 comparison, is parent > child
        if self.max_heap[pt] < self.max_heap[cd]:
            self.max_heap[pt], self.max_heap[cd] = self.max_heap[cd], self.max_heap[pt]

    def delete_max(self):
        if self.n == 0:
            return -1
        m = self.max_heap[1]
        self.max_heap[1], self.max_heap[self.n] = self.max_heap[self.n], self.max_heap[1]
        self.n -= 1
        self.sift_down(1)
        return m

    def get_operations(self):
        return self.operations

    def get_heap(self):
        return self.max_heap

