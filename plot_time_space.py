import sys
from knapsack import Knapsack
from hash_function import BinaryHash
import matplotlib.pyplot as plt
import math


def plot_stats(bu_space, bu_time, se_space_arr, se_time_arr):
    plt.rcParams.update({'font.size': 5})
    # plt.title()
    # plt.
    # plt.
    # plt.xlabel('space')
    # plt.ylabel('time')
    # plt.legend()
    # plt.ticklabel_format(useOffset=False)
    # plt.show()
    fig, ax = plt.subplots()
    # fig.loose()
    ax.set_title('Time vs Space: Traditional vs Space-Efficient Dynamic Programming')
    ax.set_xlabel('space')
    ax.set_ylabel('time')
    # ax.plot(bu_space, bu_time, 'ro', label='Traditional Method')
    ax.plot(se_space_arr, se_time_arr, 'bo', label='Space Efficient')

    # for i, v in enumerate(values):
    #     ax.text(i, v + 25, "%d" % v, ha="center")
    # plt.ylim(-10, 595)

    ax.legend()
    plt.show()


def plot_compare(ks):
    n = len(ks.items())
    W = ks.capacity()
    bu_time = ks.bu_cpu_time()

    k_array = [pow(2, n), pow(2, n - 1), int(W/2), W]  # 2^n, 2^n-1, W/2, W/128,W
    # k_array = [pow(2, n - 1)]
    # k_labels = []
    se_times = []
    se_h_items = []
    se_empty_buckets = []
    for k in k_array:
        print(k)
        bin_hash = BinaryHash(len(ks.items()), W, k, ks.items())
        bin_hash.compute()
        se_times.append(round(bin_hash.cpu_time(), 2))
        se_h_items.append(bin_hash.debug_h_items())
        se_empty_buckets.append(bin_hash.debug_empty_bucket())

    print()
    plot_stats(n * W, bu_time, k_array, se_times)
    for i in range(len(k_array)):
        print(F"For K of {k_array[i]}:")
        print(F"items: {se_h_items[i]}")
        print(F"Empty buckets: {se_empty_buckets[i]}")
        print(F"Array of Space Efficient cpu-time: {se_times[i]}")
        print()
