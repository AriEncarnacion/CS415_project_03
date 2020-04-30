import time
import sys


class BottomUp:
    def __init__(self, items, capacity):
        self.__items = items
        self.__n = len(items)
        self.__W = capacity
        self.__opt_subset = []
        self.__table = [[-1 for col in range(self.__W + 1)] for row in range(self.__n + 1)]
        self.__cpu_time = 0

    def compute(self):
        # computes optimal value, subset and cpu time
        self.__compute_opt_subset()

    def __fill_table(self):
        for row in range(self.__n + 1):
            self.__table[row][0] = 0

        for col in range(self.__W + 1):
            self.__table[0][col] = 0

        # todo need to revamp __F to be bottom-up
        for i in range(self.__n + 1):
            for j in range(self.__W + 1):
                self.__table[i][j] = self.__F(i, j)

    def __F(self, i, j):
        if i == 0:
            return 0

        if j == 0:
            return 0

        if i > 0 and j > 0:
            v = self.__items[i-1][0]
            w = self.__items[i-1][1]
        else:
            v, w = 0, 0



        if j - w >= 0:
            return max(self.__F(i - 1, j), v + self.__F(i - 1, j - w))

        return self.__F(i - 1, j)

    def __compute_opt_subset(self):
        t0 = time.perf_counter()
        self.__fill_table()  # compute F table

        # self.__table[i][j]
        j = self.__W
        i = self.__n

        while j > 0:
            v = self.__items[i - 1][0]
            w = self.__items[i - 1][1]
            if v + self.__table[i - 1][j - w] > self.__table[i - 1][j]:
                self.__opt_subset.append(i)
                j -= self.__items[i - 1][1]
            i -= 1

        self.__opt_subset.reverse()  # compensate for append logic
        t1 = time.perf_counter()
        self.__cpu_time += (t1 - t0)

    def opt_val(self):
        return self.__table[self.__n][self.__W]

    def opt_subset(self):
        return self.__opt_subset

    def cpu_time(self):
        return self.__cpu_time

    def space_taken(self):
        return sys.getsizeof(self.__table)

    def debug_print_table(self):
        print("Dynamic programming table")
        for row in self.__table:
            print(row)
        print("---------")




