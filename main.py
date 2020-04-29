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
bu_space = ks.bu_table_space()

print(F"Knapsack capacity = {cap}. Total number of items = {tot_items}")
print()

print(F"Traditional Dynamic Programming Optimal value: {bu_opt_val}")
print(F"Traditional Dynamic Programming Optimal subset: {bu_opt_set}")
print(F"Traditional Dynamic Programming Time Taken: {bu_cpu_time}")
print(F"Traditional Dynamic Programming Space Taken: {bu_space}")

print()
k = int(math.log(ks.capacity())/math.log(2))
print("k is:", k)
bin_hash = BinaryHash(len(ks.items()), ks.capacity(), k, ks.items())
bin_hash.hash_items()
print()

# Greedy Sort
gs = GreedySort(ks.values(), ks.weights(), ks.capacity())
gs.calc_opt_value()
gs.print()

# Greedy Head
gh = GreedyHeap(ks.values(), ks.weights(), ks.capacity())
gh.calc_opt_value()
gh.print()
