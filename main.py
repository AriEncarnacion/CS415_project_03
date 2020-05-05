from knapsack import Knapsack
from greedy_sort import GreedySort
from hash_function import BinaryHash
from greedy_heap import GreedyHeap
import sys
import math
import plot_dp_time_space as plt_cmp

# Put client and test logic here

file_num = str(sys.argv[9])

capacity_file = './KnapsackTestData/p' + file_num.rjust(2, '0') + '_c.txt'
values_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_v.txt"
weights_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_w.txt"

print(F"File containing the capacity, weights, and values are: "
      F"{capacity_file}, {values_file}, {weights_file}")
print()

ks = Knapsack(capacity_file, values_file, weights_file, "bu")

W = ks.capacity()
n = len(ks.items())

ks.bu_compute()  # must compute before any other bu method

# print("Plotting to compare...")
# plt_cmp.plot_compare(ks)

ks.bu_print_report()

k = int(math.pow(2, n - 4))  # k = 2^n-2
bin_hash = BinaryHash(n, W, k, ks.items())
bin_hash.compute()

bin_hash.print_report()

# print()
# print("Debug:")
# bin_hash.debug_print_table()  # NOT recommended for large inputs
# print(F"K is {k}, hash table size is {bin_hash.debug_table_size()}")
# avg_LL_sz = bin_hash.debug_avg_LL_sizes()
# hi_LL_sz = bin_hash.debug_highest_LL_size()
# print("Average Length of each linked list is:", round(avg_LL_sz, 2))  # NOT recommended for large inputs
# print("Highest length of all linked lists is:", int(hi_LL_sz))
# print()

# Greedy Sort
gs = GreedySort(ks.values(), ks.weights(), ks.capacity())
gs.calc_opt_value()
gs.print()

# Greedy Heap
gh = GreedyHeap(ks.values(), ks.weights(), ks.capacity())
gh.calc_opt_value()
gh.print()
