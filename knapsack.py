import bottom_up as bu


class Knapsack:
    """Class to hold knapsack related data. Namely Capacity, available items, and the weights for those items
    capacity is a single number value. values and weights are lists of numbers."""

    def __init__(self, c_input, v_input, w_input, method):
        self.__capacity = 0
        self.__values = []
        self.__weights = []
        self.__items = []

        c_file = open(c_input)
        for line in c_file:
            num = line.strip()
            self.__capacity = int(num)
        c_file.close()

        v_file = open(v_input)
        for line in v_file:
            num = line.strip()
            self.__values.append(int(num))
        v_file.close()

        w_file = open(w_input)
        for line in w_file:
            num = line.strip()
            self.__weights.append(int(num))

        for i in range(len(self.__values)):
            self.__items.append((self.__values[i], self.__weights[i]))

        if method == "bu":
            self.__bup = bu.BottomUp(self.__items, self.__capacity)

    def capacity(self):
        return self.__capacity

    def values(self):
        return self.__values

    def weights(self):
        return self.__weights

    def items(self):
        # returns list of tuples containing (value, weight)
        return self.__items

    def bu_compute(self):
        self.__bup.compute()

    def bu_opt_val(self):
        return self.__bup.opt_val()

    def bu_opt_sub_set(self):
        return self.__bup.opt_subset()

    def bu_cpu_time(self):
        return round(self.__bup.cpu_time(), 6)

    def bu_table_space(self):
        return self.__bup.space_taken()
