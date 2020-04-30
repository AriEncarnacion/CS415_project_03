from knapsack import Knapsack
from greedy_sort import GreedySort
from hash_function import BinaryHash
from greedy_heap import GreedyHeap
import sys
import math
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

bu_opt_set = ks.bu_opt_sub_set()
bu_opt_val = ks.bu_opt_val()
bu_cpu_time = ks.bu_cpu_time()

print(F"Knapsack capacity = {cap}. Total number of items = {tot_items}")
print()

print(F"Traditional Dynamic Programming Optimal value: {bu_opt_val}")
print(F"Traditional Dynamic Programming Optimal subset: {bu_opt_set}")
print(F"Traditional Dynamic Programming Time Taken: {bu_cpu_time}")

print()

# k = int(math.log(ks.capacity())/math.log(2))
k = 2 * ks.capacity()
bin_hash = BinaryHash(len(ks.items()), ks.capacity(), k, ks.items())

bin_hash.compute()

bh_opt_set = []
bh_opt_val = bin_hash.opt_val()
bh_cpu_time = bin_hash.cpu_time()

print("Space-efficient Dynamic Programming Optimal value:", bh_opt_val)
print("Space-efficient Dynamic Programming Optimal subset:NOT DONE", bh_opt_set)
print("Space-efficient Dynamic Programming Time Taken:", bh_cpu_time)
print("Space-efficient Dynamic Programming Space Taken:", k)

print()
print("Debug:")
# bin_hash.debug_print_table()  # NOT recommended for large inputs
# print(F"K is {k}, hash table size is {bin_hash.debug_table_size()}")
print("Average Length of each linked list is:", int(bin_hash.debug_avg_LL_sizes()))
print("Highest length of all linked lists is:", bin_hash.debug_highest_LL_size())
print()


# # Greedy Sort
# gs = GreedySort(ks.values(), ks.weights(), ks.capacity())
# gs.calc_opt_value()
# gs.print()
#
# # Greedy Head
# gh = GreedyHeap(ks.values(), ks.weights(), ks.capacity())
# gh.calc_opt_value()
# gh.print()
