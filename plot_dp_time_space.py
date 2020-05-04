import sys
from knapsack import Knapsack
from hash_function import BinaryHash
import matplotlib.pyplot as plt
import math
import time as tm


def plot_stats(bu_space, bu_time, se_space_arr, se_time_arr, space_labels):
    fig, ax = plt.subplots()
    ax.set_title('Time vs Space: Traditional vs Space-Efficient Dynamic Programming')
    ax.set_xlabel('space')
    ax.set_ylabel('time')

    # ax.plot(bu_space, bu_time, 'ro', label='Traditional Method')  # plot traditional method
    ax.plot(se_space_arr, se_time_arr, 'bo', label='Space Efficient')  # plot space efficient method

    cords = list(zip(se_space_arr, se_time_arr))
    it = 0
    for cord in cords:
        # lbl = "k=" + space_labels[it] + "=" + str(cord[0])
        lbl = space_labels[it]
        ax.annotate(lbl, xy=(cord[0], cord[1]), xytext=(0, 7), textcoords='offset pixels')
        it += 1

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1))

    plt.tight_layout()

    stamp = tm.ctime(tm.time())
    fn = 'GenPlots/fig ' + stamp + '.png'
    plt.savefig(fn)
    plt.show()


def plot_compare(ks):
    n = len(ks.items())
    W = ks.capacity()
    ks_items = ks.items()
    bu_time = ks.bu_cpu_time()
    del ks

    # TODO: ensure order in which values are tested dont compromise
    	# the time complexity. Test 2^n-4 2^n-10 in both combinations

    # W, W/2, 2^log(W), n * (W/2), 2^n-m [ 10 < m < n]
    k_array = [W, int(W/2), int(pow(2, math.log2(W))), int(n * (W/2))]
    k_labels = [r'$W$', r'$\frac{W}{2}$', r'$2^{\log{W}}$', r'$n*\frac{W}{2}$']
    for m in range(0, 11):
        k_array.append(int(pow(2, n - m)))
        if m == 0:
            k_labels.append(r'$2^{n}$')
        else:
            k_labels.append('$2^{n-%i}$' % m)
    print(k_array)
    print(k_labels)

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
