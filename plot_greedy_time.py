from knapsack import Knapsack
from greedy_sort import GreedySort
from greedy_heap import GreedyHeap
import matplotlib.pyplot as plt
import time as tm
import math

files = [str(i) for i in range(0, 9)]
l_dir = './GenPlots'
prefix = '/g_plot_'
ext = '.png'


def get_knapsack(file_num):
    capacity_file = './KnapsackTestData/p' + file_num.rjust(2, '0') + '_c.txt'
    values_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_v.txt"
    weights_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_w.txt"

    return Knapsack(capacity_file, values_file, weights_file, "")


def get_gs_ops(v, w, c):
    gs = GreedySort(v, w, c)
    gs.calc_opt_value()

    return gs.get_ops()


def get_gs_subset(v, w, c):
    gs = GreedySort(v, w, c)
    gs.calc_opt_value()

    return gs.get_subset()


def get_gh_ops(v, w, c):
    gh = GreedyHeap(v, w, c)
    gh.calc_opt_value()

    return gh.get_ops()


def get_gh_subset(v, w, c):
    gh = GreedyHeap(v, w, c)
    gh.calc_opt_value()

    return gh.get_subset()


def plot_times(data):
    n_list, gs_times, gh_times, k_list = zip(*data)

    fig, ax = plt.subplots()
    plt.scatter(n_list, gs_times, marker='X', label='Sort-Based')
    plt.scatter(n_list, gh_times, marker='P', label='Heap-Based')
    plt.xlabel("SIZE (N)", color='black', fontweight='bold')
    plt.ylabel("OPERATIONS (TIME)", color='black', fontweight='bold')
    n_th = len(n_list)
    for file in range(n_th):
        x = data[file][0]
        if file == 4:
            y = 5
        else:
            y = 2
        ax.annotate(f"p{str(file).rjust(2, '0')}", (x, y),
                    ha='right', va='center', fontsize=6, style='normal')

    ax.legend()
    plt.savefig(l_dir + prefix + tm.ctime(tm.time()) + ext)
    plt.show()


def annotate_plot_times(data):
    n_list, gs_times, gh_times, k_list = zip(*data)
    last = len(n_list) - 1

    fig, ax = plt.subplots()
    plt.scatter(n_list, gs_times, marker='X', label='Sort-Based')
    plt.scatter(n_list, gh_times, marker='P', label='Heap-Based')
    plt.xlabel("SIZE (N)", color='black', fontweight='bold')
    plt.ylabel("OPERATIONS (TIME)", color='black', fontweight='bold')

    n_th = len(n_list)
    for file in range(n_th-1):
        x = data[file][0]
        if file == 4:
            y = 5
        else:
            y = 2
        ax.annotate(f"p{str(file).rjust(2, '0')}", (x, y),
                    ha='right', va='center', fontsize=6, style='normal')

    ax.annotate(f"p08_c/2: ops={gs_times[last]}, k={k_list[last]}",
                (n_list[last], gs_times[last]), (n_list[last] - 2, gs_times[last]),
                ha='right', va='center', fontsize=7, style='italic',
                arrowprops=dict(arrowstyle='-',
                                shrinkA=5,
                                shrinkB=5,
                                fc="k", ec="k")
                )
    ax.annotate(f"p08_c: ops={gs_times[last - 1]}, k={k_list[last - 1]}",
                (n_list[last - 1], gs_times[last - 1]), (n_list[last - 1] - 2, gs_times[last - 1]),
                ha='right', va='center', fontsize=7, style='italic',
                arrowprops=dict(arrowstyle='-',
                                shrinkA=5,
                                shrinkB=5,
                                fc="k", ec="k")
                )

    ax.annotate(f"p08_c/2: ops={gh_times[last]}, k={k_list[last]}",
                (n_list[last], gh_times[last]), (n_list[last] - 2, gh_times[last]),
                ha='right', va='center', fontsize=9, style='italic',
                arrowprops=dict(arrowstyle='-',
                                shrinkA=5,
                                shrinkB=5,
                                fc="k", ec="k")
                )
    ax.annotate(f"p08_c: ops={gh_times[last - 1]}, k={k_list[last - 1]}",
                (n_list[last - 1], gh_times[last - 1]), (n_list[last - 1] - 2, gh_times[last - 1]),
                ha='right', va='center', fontsize=9, style='italic',
                arrowprops=dict(arrowstyle='-',
                                shrinkA=5,
                                shrinkB=5,
                                fc="k", ec="k")
                )
    ax.legend()
    plt.savefig(l_dir + prefix + 'anno_' + tm.ctime(tm.time()) + ext)
    plt.show()


def get_times(file_nums):  # Takes list of file numbers
    plot_data = []

    for file in file_nums:
        ks = get_knapsack(file)
        v, w, c = ks.values(), ks.weights(), ks.capacity()
        size = (len(ks.items()))
        gs = get_gs_ops(v, w, c)
        gh = get_gh_ops(v, w, c)
        k = len(get_gs_subset(v, w, c))
        plot_data.append((size, gs, gh, k))

    return plot_data


ks8 = get_knapsack('8')
new_v8, new_w8, new_c8 = ks8.values(), ks8.weights(), ks8.capacity() // 2

p08_subsets = []
g_data = get_times(files)
n = len(g_data)

print(f"Original p08 Data\n"
      f"n: {g_data[n - 1][0]} | sort ops: {g_data[n - 1][1]} | heap ops: {g_data[n - 1][2]}"
      f" | k: {g_data[n - 1][3]}")
plot_times(g_data)

# ----- Plot Data additional p08 knapsack with W/2 ----- #
ks8 = get_knapsack('8')
v8, w8, c8 = ks8.values(), ks8.weights(), ks8.capacity() // 2

new_data = (len(ks8.items()), get_gs_ops(v8, w8, c8),
            get_gh_ops(v8, w8, c8), len(get_gs_subset(v8, w8, c8)))
g_data.append(new_data)
n += 1
print(f"Capacity/2 p08 Data\n"
      f"n: {g_data[n - 1][0]} | sort ops: {g_data[n - 1][1]} | heap ops: {g_data[n - 1][2]}"
      f" | k: {g_data[n - 1][3]}")
annotate_plot_times(g_data)
