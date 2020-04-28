import math as m
import knapsack as ks

class BinaryHash:

    def __init__(self, n, W, k, items):
        self.__h_table =  [None] * k
        self.__b_n = int(m.ceil(m.log2(n + 1)))
        self.__b_W = int(m.ceil(m.log2(W + 1)))
        self.__items = items

    def build_key(self):
        print("--------------------------------------------------------")
        print("-----START debug statements BinaryHash::build_key()-----")
        print("--------------------------------------------------------")
        print("b_n:", self.__b_n)
        print("b_w", self.__b_W)

        i = self.__items[0][0]
        j = self.__items[0][1]
        r_i = format(i, "b")
        r_j = format(j, "b")
        print("i:", i)
        print("j:", j)
        print("binary of i:", r_i)
        print("binary of j:", r_j)

        while len(r_i) < self.__b_n:
            r_i = "0" + r_i

        while len(r_j) < self.__b_W:
            r_j = "0" + r_j

        print("adjusted r_i:", r_i)
        print("adjusted r_j:", r_j)

        r_ij = "1" + r_i + r_j
        print("r_ij:", r_ij)
        print("------------------------------------------------------")
        print("-----END debug statements BinaryHash::build_key()-----")
        print("------------------------------------------------------")

        return r_ij
