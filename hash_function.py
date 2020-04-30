import math as m


class BinaryHash:

    def __init__(self, n, W, k, items):
        self.__h_table = [[] for _ in range(k)]  # makes array of size k. holds (value, key)
        self.__k = k
        self.__n = n
        self.__W = W
        self.__b_n = int(m.ceil(m.log2(n + 1)))
        self.__b_W = int(m.ceil(m.log2(W + 1)))
        self.__items = items

    def __h(self, i, j):
        print("------------------------------------------------")
        print("-----START debug statements BinaryHash::h()-----")
        print("------------------------------------------------")
        print('i:', i)
        print('j:', j)
        print("b_n:", self.__b_n)
        print("b_w:", self.__b_W)
        #

        r_i = format(i, "b")
        r_j = format(j, "b")
        print("binary of i:", r_i)
        print("binary of j:", r_j)

        print("bits in b_n:", self.__b_n, "bits in r_i:", len(r_i))
        print("bits in b_W:", self.__b_W, "bits in r_j:", len(r_j)
              )

        while len(r_i) < self.__b_n:
            r_i = "0" + r_i

        while len(r_j) < self.__b_W:
            r_j = "0" + r_j

        print("adjusted r_i:", r_i)
        print("adjusted r_j:", r_j)

        r_ij = "0b" + "1" + r_i + r_j  # build r_ij
        dec_r_ij = int(r_ij, 2)  # convery r_ij to decimal
        print("r_ij:", r_ij)
        print("decimal_r_ij:", dec_r_ij)
        print("----------------------------------------------")
        print("-----END debug statements BinaryHash::h()-----")
        print("----------------------------------------------")
        return dec_r_ij

    def hash_items(self):
        for i in range(self.__n + 1):
            for j in range(self.__W + 1):
                self.__hash_mem_func(i, j)
        # for item in self.__items:
        #     key = self.__h(item[0], item[1])
        #     #
        #     # h_idx = key % self.__k
        #     # hash_item = (item[0], item[1], key)
        #     # self.__h_table[h_idx].append(hash_item)
        #     print(F"key for item {item} is {key}")
        #     self.__hash_mem_func()

    def debug_print_table(self):
        print(self.__h_table)

    def __search_table(self, i, j):
        key = self.__h(i, j)
        h_idx = key % self.__k
        print(F"Searching table for key {key} at index {h_idx}.")

        found = -1
        for entry in self.__h_table[h_idx]:
            if entry[1] == key:
                found = entry[0]
        return found
        # if key[1] in self.__h_table[h_idx]:
        #     return search_item
        # else:
        #     return -1

    def __insert_table(self, i, j, val):
        key = self.__h(i, j)
        h_idx = key % self.__k
        insert_item = (val, key)
        print(F"Inserting {insert_item} into table at index {h_idx}.")
        self.__h_table[h_idx].append(insert_item)

    def __hash_mem_func(self, i, j):
        if i == 0 or j == 0:
            return 0

        if self.__search_table(i, j) == -1:
            w = self.__items[i - 1][1]
            if j < w:
                v = self.__hash_mem_func(i - 1, j)
            else:
                v = max(self.__hash_mem_func(i - 1, j), self.__items[i - 1][0] + self.__hash_mem_func(i - 1, j - w))
            self.__insert_table(i, j, v)

        return self.__search_table(i, j)

    def debug_table_size(self):
        return len(self.__h_table)

    def debug_LL_sizes(self):
        sizes = []
        for lst in self.__h_table:
            sizes.append(len(lst))
        return sizes
