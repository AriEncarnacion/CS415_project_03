import sys
from knapsack import Knapsack
from hash_function import BinaryHash
import matplotlib.pyplot as plt
import math


def plot_stats(bu_space, bu_time, se_space_arr, se_time_arr, space_labels):
    fig, ax = plt.subplots()
    ax.set_title('Time vs Space: Traditional vs Space-Efficient Dynamic Programming')
    ax.set_xlabel('space')
    ax.set_ylabel('time')

    # ax.plot(bu_space, bu_time, 'ro', label='Traditional Method')
    ax.plot(se_space_arr, se_time_arr, 'bo', label='Space Efficient')

    cords = list(zip(se_space_arr, se_time_arr))
    it = 0
    for cord in cords:
        lbl = "k=" + space_labels[it] + "=" + str(cord[0])
        ax.annotate(lbl, xy=(cord[0], cord[1]), xytext=(7, -1), textcoords='offset pixels')
        it += 1

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))

    plt.tight_layout()

    plt.savefig('fig.png')
    plt.show()


def plot_compare(ks):
    n = len(ks.items())
    W = ks.capacity()
    ks_items = ks.items()
    bu_time = ks.bu_cpu_time()
    del ks

    k_array = [pow(2, n), pow(2, n - 1), pow(2, n - 2), int(W/2), W]  # 2^n, 2^n-1, 2^n-2, W/2, W
    k_labels = [r'$2^n$', r'$2^{n-1}$', r'$2^{n-2}$', r'$\frac{W}{2}$', r'$W$']
    k_array.sort()
    se_times = []
    se_h_items = []
    se_empty_buckets = []
    for k in k_array:
        print(k)
        bin_hash = BinaryHash(n, W, k, ks_items)
        bin_hash.compute()
        se_times.append(round(bin_hash.cpu_time(), 4))
        se_h_items.append(bin_hash.debug_h_items())
        se_empty_buckets.append(bin_hash.debug_empty_bucket())
        del bin_hash

    print()
    plot_stats(n * W, bu_time, k_array, se_times, k_labels)
    for i in range(len(k_array)):
        print(F"For K of {k_array[i]}:")
        print(F"items: {se_h_items[i]}")
        print(F"Empty buckets: {se_empty_buckets[i]}")
        print(F"Array of Space Efficient cpu-time: {se_times[i]}")
        print()
