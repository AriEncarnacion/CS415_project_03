import knapsack as ks

# Put client and test logic here

capacity_file = "./KnapsackTestData/p03_c.txt"
values_file = "./KnapsackTestData/p03_v.txt"
weights_file = "./KnapsackTestData/p03_w.txt"

ex_ks = ks.Knapsack(capacity_file, values_file, weights_file)

print("ex_ks capacity", ex_ks.capacity())
print("ex_ks values", ex_ks.values())
print("ex_ks weights", ex_ks.weights())
