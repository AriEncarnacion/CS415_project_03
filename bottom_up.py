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
        t0 = time.perf_counter()
        self.__fill_table()  # compute F table
        self.__compute_opt_subset(self.__n, self.__W)
        t1 = time.perf_counter()
        self.__cpu_time += (t1 - t0)
        self.__opt_subset.reverse()  # compensate for append logic

    def __fill_table(self):
        for row in range(self.__n + 1):
            self.__table[row][0] = 0

        for col in range(self.__W + 1):
            self.__table[0][col] = 0

        self.__F(self.__n, self.__W)

    def __F(self, i, j):
        if i == 0 or j == 0:
            return 0

        v = self.__items[i - 1][0]
        w = self.__items[i - 1][1]

        if j - w >= 0:
            self.__table[i][j] = max(self.__F(i - 1, j), v + self.__F(i - 1, j - w))
        else:
            self.__table[i][j] = self.__F(i - 1, j)

        return self.__table[i][j]

    def __compute_opt_subset(self, i, j):
        v = self.__items[i - 1][0]
        w = self.__items[i - 1][1]

        if i == 0 or j == 0:
            return 0

        if j - w >= 0:
            take = v + self.__table[i - 1][j - w]
            drop = self.__table[i - 1][j]
            if take > drop:
                self.__opt_subset.append(i)
                return self.__compute_opt_subset(i - 1, j - w)

        return self.__compute_opt_subset(i - 1, j)

        # while j > 0:
        #     v = self.__items[i - 1][0]
        #     w = self.__items[i - 1][1]
        #     if v + self.__table[i - 1][j - w] > self.__table[i - 1][j]:
        #         self.__opt_subset.append(i)
        #         j -= self.__items[i - 1][1]
        #     i -= 1

    def opt_val(self):
        return self.__table[self.__n][self.__W]

    def opt_subset(self):
        return self.__opt_subset

    def cpu_time(self):
        return self.__cpu_time

    def debug_print_table(self):
        print("Dynamic programming table")
        for row in self.__table:
            print(row)
        print("---------")




