from knapsack import Knapsack
from greedy_sort import GreedySort
from greedy_heap import GreedyHeap
import matplotlib.pyplot as plt
import time as tm
import matplotlib.patches as mpatches
import numpy as nmp
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def get_knapsack(file_num):
    capacity_file = './KnapsackTestData/p' + file_num.rjust(2, '0') + '_c.txt'
    values_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_v.txt"
    weights_file = "./KnapsackTestData/p" + file_num.rjust(2, "0") + "_w.txt"

    return Knapsack(capacity_file, values_file, weights_file, "")


def get_gs_ops(v, w, c):
    gs = GreedySort(v, w, c)
    gs.calc_opt_value()

    return gs.get_ops()


def get_gh_ops(v, w, c):
    gh = GreedyHeap(v, w, c)
    gh.calc_opt_value()

    return gh.get_ops()


def plot_times(data):

    n_list, gs_times, gh_times = zip(*data)

    fig, ax = plt.subplots()
    plt.scatter(n_list, gs_times, marker='X', label='Sort-Based')
    plt.scatter(n_list, gh_times, marker='P', label='Heap-Based')
    plt.xlabel("SIZE (N)", color='maroon', fontweight='bold')
    plt.ylabel("OPERATIONS (TIME)", color='maroon', fontweight='bold')

    # adj_n = list(dict.fromkeys(n_list))
    # print(adj_n)
    # for file in range(len(adj_n)):
    #     ax.annotate(f"n={adj_n[file]}", (adj_n[file], gh_times[file]+4),
    #                 ha='right', va='center', fontsize=7, style='normal')
    ax.legend()
    plt.savefig(l_dir + prefix + 'anno_' + tm.ctime(tm.time()) + ext)
    plt.show()


def annotate_plot_times(data):
    n_list, gs_times, gh_times = zip(*data)
    last = len(n_list) - 1


    fig, ax = plt.subplots()
    plt.scatter(n_list, gs_times, marker='X', label='Sort-Based')
    plt.scatter(n_list, gh_times, marker='P', label='Heap-Based')
    plt.xlabel("SIZE (N)", color='maroon', fontweight='bold')
    plt.ylabel("OPERATIONS (TIME)", color='maroon', fontweight='bold')

    ax.annotate("p08_c/2", (n_list[last], gh_times[last]), (n_list[last] - 2, gh_times[last]),
                ha='right', va='center', fontsize=9, style='italic',
                arrowprops=dict(arrowstyle='->',
                                shrinkA=5,
                                shrinkB=5,
                                fc="k", ec="k")
                )
    ax.annotate("p08_c", (n_list[last - 1], gh_times[last - 1]), (n_list[last - 1] - 2, gh_times[last - 1]),
                ha='right', va='center', fontsize=9, style='italic',
                arrowprops=dict(arrowstyle='->',
                                shrinkA=5,
                                shrinkB=5,
                                fc="k", ec="k")
                )
    plt.savefig(l_dir + prefix + 'anno_' + tm.ctime(tm.time()) + ext)
    plt.show()


def get_times(file_nums):  # Takes list of file numbers
    plot_data = []

    for file in file_nums:
        ks = get_knapsack(file)
        v, w, c = ks.values(), ks.weights(), ks.capacity()
        n = (len(ks.items()))
        gs = get_gs_ops(v, w, c)
        gh = get_gh_ops(v, w, c)
        plot_data.append((n, gs, gh))

    return plot_data


files = [str(i) for i in range(0, 9)]
l_dir = './GenPlots'
prefix = '/g_plot_'
ext = '.png'

g_data = get_times(files)

plot_times(g_data)

# ----- Plot Data additional p08 knapsack with W/2 ----- #
ks8 = get_knapsack('8')
v8, w8, c8 = ks8.values(), ks8.weights(), ks8.capacity()//2

new_data = (len(ks8.items()), get_gs_ops(v8, w8, c8), get_gh_ops(v8, w8, c8))
g_data.append(new_data)

annotate_plot_times(g_data)

