from max_heap import MaxHeap


class GreedyHeap:

    def __init__(self, values, weights, capacity):
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.ratios = list(map(lambda x, y: x / y, values, weights))
        self.subset = []
        self.opt_value = 0
        self.heap = MaxHeap(self.ratios)

    def calc_opt_value(self):
        self.heap.build_heap()

        cur_capacity = 0
        index = self.ratios.index(self.heap.delete_max())

        while index != -1 and cur_capacity + self.weights[index] < self.capacity:
            cur_capacity += self.weights[index]
            self.opt_value += self.values[index]
            self.subset.append(index + 1)
            index = self.ratios.index(self.heap.delete_max())

        self.subset.sort()

    def print(self):
        print()
        print(F"Heap-Based Greedy Approach Optimal Value: {self.opt_value}")
        print(F"Heap-Based Greedy Approach Optimal subset: {self.subset}")
        print(F"Heap-Based Greedy Approach Number of Operations: {self.heap.get_operations()}")

    def get_subset(self):
        return self.subset

    def build_heap(self):
        self.heap.build_heap()

    def get_ops(self):
        return self.heap.get_operations()

    def get_heap(self):
        return self.heap.max_heap
