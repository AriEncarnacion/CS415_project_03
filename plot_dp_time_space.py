import sys
from knapsack import Knapsack
from hash_function import BinaryHash
import matplotlib.pyplot as plt
import math
import time as tm

file_num = '8'


def plot_stats(bu_space, bu_time, se_space_arr, se_time_arr, space_labels, opt_val, opt_time, opt_lbl):
    fig, ax = plt.subplots()
    ax.set_title('Time vs Space: Traditional vs Space-Efficient Dynamic Programming')
    ax.set_xlabel('space')
    ax.set_ylabel('time')

    # ax.plot(bu_space, bu_time, 'ro', label='Traditional Method')  # uncomment to plot traditional method
    ax.plot(se_space_arr, se_time_arr, 'bo', label='Space Efficient')  # plot space efficient method
    ax.plot(opt_val, opt_time, 'g*', label='Optimal K')

    cords = list(zip(se_space_arr, se_time_arr))
    it = 0
    for cord in cords:
        lbl = space_labels[it]
        ax.annotate(lbl, xy=(cord[0], cord[1]), xytext=(0, 7), textcoords='offset pixels')
        it += 1

    ax.annotate(opt_lbl, xy=(opt_val, opt_time), xytext=(0, 7), textcoords='offset pixels')

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))

    plt.tight_layout()

    stamp = tm.ctime(tm.time())
    fn = 'GenPlots/Dyn_Prog_Time_Space' + stamp + '.png'
    plt.savefig(fn)
    plt.show()
    print(F"Plot saved as '{fn}'")
    print()


def plot_compare(ks):
    n = len(ks.items())
    W = ks.capacity()
    ks_items = ks.items()
    bu_time = ks.bu_cpu_time()
    del ks

    m = math.floor(math.log2(n))
    k_opt = pow(2, math.floor(math.log2(n * W) - m))
    k_opt_lbl = r'$2^{\log(n*W)- \log_2{n}}$'
    print("Optimal K:", k_opt_lbl, "=", k_opt)

    k_array = []
    k_labels = []
    for m in range(1, 8):
        k_array.append(pow(2, math.floor(math.log2(n * W) - m)))
        k_labels.append(r'$2^{\log(nW)-%i}$' % m)

    print(k_array)
    print(k_labels)

    bin_hash = BinaryHash(n, W, k_opt, ks_items)
    bin_hash.compute()
    k_opt_time = bin_hash.cpu_time()
    del bin_hash

    se_times = []
    for k in k_array:
        print(k)
        bin_hash = BinaryHash(n, W, k, ks_items)
        bin_hash.compute()
        se_times.append(round(bin_hash.cpu_time(), 4))
        del bin_hash

    print()
    plot_stats(n * W, bu_time, k_array, se_times, k_labels, k_opt, k_opt_time,k_opt_lbl)
    print(F"Optimal k: {k_opt_lbl}:")
    print(F"Optimal K value: {k_opt}")
    print(F"Optimal K time: {round(k_opt_time, 4)}")
    print()

    for i in range(len(k_array)):
        print(F"For K of {k_labels[i]}:")
        print(F"K numerical value: {k_array[i]}")
        print(F"Array of Space Efficient cpu-time: {se_times[i]}")
        print()

capacity_file = './KnapsackTestData/p' + file_num.rjust(2, '0') + '_c.txt'
values_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_v.txt"
weights_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_w.txt"

print(F"File containing the capacity, weights, and values are: "
      F"{capacity_file}, {values_file}, {weights_file}")
print()

knapsack = Knapsack(capacity_file, values_file, weights_file, "bu")
knapsack.bu_compute()
plot_compare(knapsack)
