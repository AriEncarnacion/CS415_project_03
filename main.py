from knapsack import Knapsack
from greedy_sort import GreedySort
from hash_function import BinaryHash
from greedy_heap import GreedyHeap
import sys
import math
import plot_time_space as plt_cmp

# Put client and test logic here

file_num = str(sys.argv[1])

capacity_file = './KnapsackTestData/p' + file_num.rjust(2, '0') + '_c.txt'
values_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_v.txt"
weights_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_w.txt"

print(F"File containing the capacity, weights, and values are: "
      F"{capacity_file}, {values_file}, {weights_file}")
print()

ks = Knapsack(capacity_file, values_file, weights_file, "bu")

cap = ks.capacity()
tot_items = len(ks.items())

ks.bu_compute()  # must compute before any other bu method

# print("Plotting to compare...")
# plt_cmp.plot_compare(ks)

bu_opt_set = ks.bu_opt_sub_set()
bu_opt_val = ks.bu_opt_val()
bu_cpu_time = ks.bu_cpu_time()

print(F"Knapsack capacity = {cap}. Total number of items = {tot_items}")
print()

print(F"Traditional Dynamic Programming Optimal value: {bu_opt_val}")
print(F"Traditional Dynamic Programming Optimal subset: {bu_opt_set}")
print(F"Traditional Dynamic Programming Time Taken: {bu_cpu_time}")

print()

# TODO: plot K to find optimal value for space/time tradeoff.
#     Currently thinking K should be somewhere between log_2(W), W/2, and W.
#     Previously K*2 was implemented but I ran out of memory upon hashing the table.
#     Progress output has been put into hash_function::BinaryHash::compute() in order to
#     track progress
n = int(len(ks.items()))
k = int(pow(2, n-2))  # 2^n-2

bin_hash = BinaryHash(len(ks.items()), ks.capacity(), k, ks.items())

bin_hash.compute()

bh_opt_set = bin_hash.opt_subset()
bh_opt_val = bin_hash.opt_val()
bh_cpu_time = bin_hash.cpu_time()

print("Space-efficient Dynamic Programming Optimal value:", bh_opt_val)
print("Space-efficient Dynamic Programming Optimal subset:", bh_opt_set)
print("Space-efficient Dynamic Programming Time Taken:", bh_cpu_time)
print("Space-efficient Dynamic Programming Space Taken:", k)



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
