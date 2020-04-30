import math as m


class BinaryHash:

    def __init__(self, n, W, k, items):
        self.__h_table = [[()] for _ in range(k)]  # makes array of size k. holds (value, key)
        self.__k = k
        self.__b_n = int(m.ceil(m.log2(n + 1)))
        self.__b_W = int(m.ceil(m.log2(W + 1)))
        self.__items = items

    def __h(self, i, j):
        # print("------------------------------------------------")
        # print("-----START debug statements BinaryHash::h()-----")
        # print("------------------------------------------------")
        # print("b_n:", self.__b_n)
        # print("b_w", self.__b_W)
        #
        r_i = format(i, "b")
        r_j = format(j, "b")
        # print("i:", i)
        # print("j:", j)
        # print("binary of i:", r_i)
        # print("binary of j:", r_j)

        while len(r_i) < self.__b_n:
            r_i = "0" + r_i

        while len(r_j) < self.__b_W:
            r_j = "0" + r_j

        # print("adjusted r_i:", r_i)
        # print("adjusted r_j:", r_j)

        r_ij = "0b" + "1" + r_i + r_j  # build r_ij
        dec_r_ij = int(r_ij, 2)  # convery r_ij to decimal
        # print("r_ij:", r_ij)
        # print("decimal_r_ij:", decimal_r_ij)
        # print("----------------------------------------------")
        # print("-----END debug statements BinaryHash::h()-----")
        # print("----------------------------------------------")
        return dec_r_ij % self.__k

    def hash_items(self):
        for item in self.__items:
            key = self.__h(item[0], item[1])
            print(F"key for item {item} is {key}")

    def debug_print_table(self):
        print(self.__h_table)
