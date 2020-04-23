import knapsack as ks
import bottom_up as bup

# Put client and test logic here

capacity_file = "./KnapsackTestData/p00_c.txt"
values_file = "./KnapsackTestData/p00_v.txt"
weights_file = "./KnapsackTestData/p00_w.txt"

ex_ks = ks.Knapsack(capacity_file, values_file, weights_file)

print("ex_ks capacity", ex_ks.capacity())
print("ex_ks values", ex_ks.values())
print("ex_ks weights", ex_ks.weights())

bup.F(ex_ks.items(), ex_ks.capacity())
