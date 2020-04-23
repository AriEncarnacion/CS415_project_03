import knapsack as ks
import bottom_up as bup

# Put client and test logic here

capacity_file = "./KnapsackTestData/p07_c.txt"
values_file = "./KnapsackTestData/p07_v.txt"
weights_file = "./KnapsackTestData/p07_w.txt"

print(F"File containing the capacity, weights, and values are: "
      F"{capacity_file}, {values_file}, {weights_file}")
print()
knapsack = ks.Knapsack(capacity_file, values_file, weights_file, "bu")

cap = knapsack.capacity()
tot_items = len(knapsack.items())

knapsack.bu_compute()  # must compute before any other bu method

bu_opt_set = knapsack.bu_opt_sub_set()
bu_opt_val = knapsack.bu_opt_val()
bu_cpu_time = knapsack.bu_cpu_time()
bu_space = knapsack.bu_table_space()

print(F"Knapsack capacity = {cap}. Total number of items = {tot_items}")
print()

print(F"Traditional Dynamic Programming Optimal value: {bu_opt_val}")
print(F"Traditional Dynamic Programming Optimal subset: {bu_opt_set}")
print(F"Traditional Dynamic Programming Time Taken: {bu_cpu_time}")
print(F"Traditional Dynamic Programming Space Taken: {bu_space}")
