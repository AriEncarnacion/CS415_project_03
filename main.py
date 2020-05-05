from knapsack import Knapsack
from greedy_sort import GreedySort
from hash_function import BinaryHash
from greedy_heap import GreedyHeap
import sys
import math

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
ks.bu_print_report()

k = int(math.pow(2, n - 4))  # k = 2^n-4
bin_hash = BinaryHash(n, W, k, ks.items())
bin_hash.compute()
bin_hash.print_report()

# Greedy Sort
gs = GreedySort(ks.values(), ks.weights(), ks.capacity())
gs.calc_opt_value()
gs.print()

# Greedy Heap
gh = GreedyHeap(ks.values(), ks.weights(), ks.capacity())
gh.calc_opt_value()
gh.print()
