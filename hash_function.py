import math as m
import time as tm
import sys


class BinaryHash:

    def __init__(self, n, W, k, items):
        self.__h_table = [[] for _ in range(k)]  # makes array of size k. holds (value, key)
        self.__k = k
        self.__n = n
        self.__W = W
        self.__b_n = int(m.ceil(m.log2(n + 1)))
        self.__b_W = int(m.ceil(m.log2(W + 1)))
        self.__items = items
        self.__opt_subset = []
        self.__cpu_time = 0
        self.__h_items = 0

    def opt_val(self):
        key = self.__h(self.__n, self.__W)
        h_idx = key % self.__k
        for entry in self.__h_table[h_idx]:
            if entry[1] == key:
                return entry[0]
        return "ERROR::hash_function::opt_val(): could not find opt_val"

    def opt_subset(self):
        return self.__opt_subset

    def cpu_time(self):
        return self.__cpu_time

    def print_report(self):
        bh_opt_set = self.__opt_subset
        bh_opt_val = self.opt_val()
        bh_cpu_time = round(self.__cpu_time, 4)

        print(F"Space-efficient Dynamic Programming Optimal value: {bh_opt_val}")
        print(F"Space-efficient Dynamic Programming Optimal subset: {bh_opt_set}")
        print(F"Space-efficient Dynamic Programming Time Taken: {bh_cpu_time}")
        print(F"Space-efficient Dynamic Programming Space Taken: k = {self.__k}")

    def compute(self):
        t0 = tm.perf_counter()
        self.__hash_mem_func(self.__n, self.__W)
        self.__compute_opt_subset(self.__n, self.__W)
        self.__opt_subset.reverse()  # compensate for append order
        t1 = tm.perf_counter()
        self.__cpu_time += (t1 - t0)

    def __compute_opt_subset(self, i, j):

        v = self.__items[i - 1][0]
        w = self.__items[i - 1][1]

        if i == 0 or j == 0:
            return 0

        if j - w >= 0:
            take = v + self.__search_table(i - 1, j - w)
            drop = self.__search_table(i - 1, j)
            if take > drop and j - w >= 0:
                self.__opt_subset.append(i)
                return self.__compute_opt_subset(i - 1, j - w)

        return self.__compute_opt_subset(i - 1, j)

    def __hash_mem_func(self, i, j):
        if i == 0 or j == 0:
            return 0

        if self.__search_table(i, j) == -1:
            v = self.__items[i - 1][0]
            w = self.__items[i - 1][1]
            if j < w:
                val = self.__hash_mem_func(i - 1, j)
            else:
                val = max(self.__hash_mem_func(i - 1, j), v + self.__hash_mem_func(i - 1, j - w))
            self.__insert_table(i, j, val)

        return self.__search_table(i, j)

    def __search_table(self, i, j):
        key = self.__h(i, j)
        h_idx = key % self.__k

        found = -1
        for entry in self.__h_table[h_idx]:
            if entry[1] == key:
                return entry[0]  # return value at h_idx
        return found

    def __insert_table(self, i, j, val):
        key = self.__h(i, j)
        h_idx = key % self.__k
        insert_item = (val, key)
        self.__h_table[h_idx].append(insert_item)
        self.__h_items += 1

    def __h(self, i, j):
        if i < 0 or j < 0:
            print(F"FATAL::hash_function::__h(i, j): i was {i} and j was {j}.")
            sys.exit(4)

        r_i = format(i, "b")
        r_j = format(j, "b")

        while len(r_i) < self.__b_n:
            r_i = "0" + r_i

        while len(r_j) < self.__b_W:
            r_j = "0" + r_j

        r_ij = "0b" + "1" + r_i + r_j  # build r_ij
        dec_r_ij = int(r_ij, 2)  # convert r_ij to decimal

        return dec_r_ij
