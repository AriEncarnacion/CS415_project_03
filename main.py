from knapsack import Knapsack
import greedy_sort as GS
from hash_function import BinaryHash

# Put client and test logic here

capacity_file = "./KnapsackTestData/p01_c.txt"
values_file = "./KnapsackTestData/p01_v.txt"
weights_file = "./KnapsackTestData/p01_w.txt"

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
k = int(len(ks.items()) * ks.capacity() / 2)
print("k is:", k)
bin_hash = BinaryHash(len(ks.items()), ks.capacity(), k, ks.items())
bin_hash.hash_items()
print()

# Greedy Sort
gs = GS.GreedySort(ks.values(), ks.weights(), ks.capacity())
gs.calc_opt_value()
gs.print()
