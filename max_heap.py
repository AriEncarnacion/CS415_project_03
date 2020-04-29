class MaxHeap:

    def __init__(self, ratios):
        self.heap = [*[0], *ratios]  # add 0 to front of heap
        self.n = len(self.heap) - 1
        self.build_operations = 0
        self.sort_operations = 0

    def build_heap(self):
        if self.n <= 1:
            return
        rmp = self.n // 2
        while rmp > 0:
            if rmp*2+1 <= self.n:
                self.swap(rmp, rmp*2+1)
            self.swap(rmp, rmp*2)
            rmp -= 1

    def sift_down(self, pt):
        while pt <= self.n // 2:
            if pt*2+1 > self.n or self.heap[pt*2] > self.heap[pt*2+1]:
                self.swap(pt, pt*2)
                pt = pt*2
            elif self.heap[pt*2] < self.heap[pt*2+1]:
                self.swap(pt, pt*2+1)
                pt = pt*2+1
            else:
                break

    def swap(self, pt, cd):
        self.build_operations += 1
        if self.heap[pt] < self.heap[cd]:
            self.heap[pt], self.heap[cd] = self.heap[cd], self.heap[pt]
            return True
        return False

    def delete_max(self):
        if self.n == 0:
            return -1
        m = self.heap[1]
        self.heap[1], self.heap[self.n] = self.heap[self.n], self.heap[1]
        self.n -= 1
        self.sift_down(1)
        return m

    def get_operations(self):
        return self.build_operations

