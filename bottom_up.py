import time
import sys


class BottomUp:
    def __init__(self, items, capacity):
        self.__items = items
        self.__n = len(items)
        self.__W = capacity
        self.__opt_subset = []
        self.__F = [[-1 for col in range(self.__W + 1)] for row in range(self.__n + 1)]
        self.__cpu_time = 0

    def compute(self):
        t0 = time.perf_counter()
        self.__fill_table()  # compute F table
        self.__compute_opt_subset(self.__n, self.__W)
        t1 = time.perf_counter()
        self.__cpu_time += (t1 - t0)
        self.__opt_subset.reverse()  # compensate for append logic

    def __fill_table(self):
        for row in range(self.__n + 1):
            self.__F[row][0] = 0

        for col in range(self.__W + 1):
            self.__F[0][col] = 0

        for i in range(1, self.__n + 1):
            for j in range(1, self.__W + 1):
                v = self.__items[i - 1][0]
                w = self.__items[i - 1][1]
                if j - w >= 0:
                    self.__F[i][j] = max(self.__F[i - 1][j], v + self.__F[i - 1][j - w])
                else:
                    self.__F[i][j] = self.__F[i - 1][j]

    def __compute_opt_subset(self, i, j):
        v = self.__items[i - 1][0]
        w = self.__items[i - 1][1]

        if i == 0 or j == 0:
            return 0

        if j - w >= 0:
            take = v + self.__F[i - 1][j - w]
            drop = self.__F[i - 1][j]
            if take > drop:
                self.__opt_subset.append(i)
                return self.__compute_opt_subset(i - 1, j - w)

        return self.__compute_opt_subset(i - 1, j)

    def opt_val(self):
        return self.__F[self.__n][self.__W]

    def opt_subset(self):
        return self.__opt_subset

    def cpu_time(self):
        return self.__cpu_time

    def print_report(self):
        bu_opt_set = self.__opt_subset
        bu_opt_val = self.__F[self.__n][self.__W]
        bu_cpu_time = round(self.__cpu_time, 4)

        print(F"Knapsack capacity = {self.__W}. Total number of items = {self.__n}")
        print()
        print(F"Traditional Dynamic Programming Optimal value: {bu_opt_val}")
        print(F"Traditional Dynamic Programming Optimal subset: {bu_opt_set}")
        print(F"Traditional Dynamic Programming Time Taken: {bu_cpu_time}")
        print(F"Traditional Dynamic Programming Space Taken: n * W = {self.__n * self.__W}")
        print()

    def debug_print_table(self):
        print("Dynamic programming table")
        for row in self.__F:
            print(row)
        print("---------")


