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
            self.sift_down(rmp)
            rmp -= 1

    def sift_down(self, pt):
        while pt <= self.n // 2:
            cd = self.largest_child(pt*2, pt*2+1)
            # print(f"Parent: {pt} ({self.heap[pt]}), Child: {cd} ({self.heap[cd]})")
            if self.swap(pt, cd):
                pt = cd
            else:
                break

    def swap(self, pt, cd):
        if self.heap[pt] < self.heap[cd]:
            self.heap[pt], self.heap[cd] = self.heap[cd], self.heap[pt]
            return True
        return False

    def largest_child(self, lt, rt):
        if rt > self.n:
            self.build_operations += 1          # count 1 operation if only one child
            return lt
        self.build_operations += 2              # count 2 operations to determine the largest child
        if self.heap[lt] > self.heap[rt]:
            return lt
        return rt

    def delete_max(self):
        if self.n == 0:
            return -1
        m = self.heap[1]
        self.heap[1], self.heap[self.n] = self.heap[self.n], self.heap[1]
        self.n -= 1
        self.sift_down(1)
        return m

    def debug_print(self):
        i = 1
        center = self.n // 2
        while i <= self.n // 2:
            if i * 2 + 1 <= self.n:
                print("     ", self.heap[i], "\n", self.heap[i * 2], " ", self.heap[i * 2 + 1])
            else:
                print("     ", self.heap[i], "\n", self.heap[i * 2])
            print()
            i += 1

    def get_heap(self):
        return self.heap

    # def sift_up(self, leaf):
    #     while leaf > 1 and self.swap(leaf // 2, leaf):
    #         self.sort_operations += 1           # count 1 for successful swap comparison
    #         leaf //= 2
    #     self.sort_operations += 1               # count 1 for last comparison

    def get_operations(self):
        return self.build_operations

