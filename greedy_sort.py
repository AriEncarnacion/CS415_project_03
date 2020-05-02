class GreedySort:
    def __init__(self, values, weights, capacity):
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.ratios = list(map(lambda x, y: x / y, values, weights))
        self.subset = []
        self.operations = 0
        self.opt_value = 0

    # Returns new sorted array
    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr
        return self.merge(self.merge_sort(arr[:len(arr) // 2]), self.merge_sort(arr[len(arr) // 2:]))

    # Helper fn: Returns single sorted array
    def merge(self, larr, rarr):
        merged = []
        i, j = 0, 0

        while i < len(larr) and j < len(rarr):
            self.operations += 1                # +1 comparison
            if larr[i] >= rarr[j]:
                merged.append(larr[i])
                i += 1
            else:
                merged.append(rarr[j])
                j += 1

        if i == len(larr):
            merged += rarr[j:]
        if j == len(rarr):
            merged += larr[i:]

        return merged

    def calc_opt_value(self):
        cur_capacity = 0
        i = 0
        s_arr = self.merge_sort(self.ratios)
        while cur_capacity + self.weights[self.ratios.index(s_arr[i])] < self.capacity:
            self.operations += 1
            index = self.ratios.index(s_arr[i])
            cur_capacity += self.weights[index]
            self.opt_value += self.values[index]
            self.subset.append(index + 1)
            i += 1

        self.subset.sort()

    def print(self):
        print()
        print(F"Greedy Approach Optimal Value: {self.opt_value}")
        print(F"Greedy Approach Optimal subset: {self.subset}")
        print(F"Greedy Approach Number of Operations: {self.operations}")

