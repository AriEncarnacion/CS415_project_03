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

    def compute(self):
        t0 = tm.perf_counter()
        print("Commencing hashing...")
        self.__hash_mem_func(self.__n, self.__W)
        print("hashing complete.")
        print("Computing optimal subset...")
        self.__compute_opt_subset(self.__n, self.__W)
        print("Optimal subset computed.")
        print("Reversing subset...")
        self.__opt_subset.reverse()
        print("Finished subset reversal.")
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
            self.__insert_table(i, j, 0)
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
        # print(F"Searching table for key {key} at index {h_idx}.")

        found = -1
        for entry in self.__h_table[h_idx]:
            if entry[1] == key:
                return entry[0]  # return value
        return found
        # if key[1] in self.__h_table[h_idx]:
        #     return search_item
        # else:
        #     return -1

    def __insert_table(self, i, j, val):
        key = self.__h(i, j)
        h_idx = key % self.__k
        insert_item = (val, key)
        # print(F"Inserting {insert_item} into table at index {h_idx}.")
        self.__h_table[h_idx].append(insert_item)

    def __h(self, i, j):
        if i < 0 or j < 0:
            print(F"FATAL::hash_function::__h(i, j): i was {i} and j was {j}.")
            sys.exit(4)
        # print("------------------------------------------------")
        # print("-----START debug statements BinaryHash::h()-----")
        # print("------------------------------------------------")
        # print('i:', i)
        # print('j:', j)
        # print("b_n:", self.__b_n)
        # print("b_w:", self.__b_W)

        r_i = format(i, "b")
        r_j = format(j, "b")
        # print("binary of i:", r_i)
        # print("binary of j:", r_j)
        #
        # print("bits in b_n:", self.__b_n, "bits in r_i:", len(r_i))
        # print("bits in b_W:", self.__b_W, "bits in r_j:", len(r_j))

        while len(r_i) < self.__b_n:
            r_i = "0" + r_i

        while len(r_j) < self.__b_W:
            r_j = "0" + r_j

        # print("adjusted r_i:", r_i)
        # print("adjusted r_j:", r_j)

        r_ij = "0b" + "1" + r_i + r_j  # build r_ij
        dec_r_ij = int(r_ij, 2)  # convery r_ij to decimal
        # print("r_ij:", r_ij)
        # print("decimal_r_ij:", dec_r_ij)
        # print("----------------------------------------------")
        # print("-----END debug statements BinaryHash::h()-----")
        # print("----------------------------------------------")
        return dec_r_ij

    def debug_table_size(self):
        return len(self.__h_table)

    def debug_highest_LL_size(self):
        size = 0
        for lst in self.__h_table:
            if len(lst) > size:
                size = len(lst)
        return size

    def debug_print_table(self):
        for row in self.__h_table:
            print(row)

    def debug_avg_LL_sizes(self):
        sm = 0
        for lst in self.__h_table:
            sm += len(lst)
        return sm / len(self.__h_table)
