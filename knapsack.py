class Knapsack:
    """Class to hold knapsack related data. Namely Capacity, available items, and the weights for those items
    capacity is a single number value. values and weights are lists of numbers."""

    def __init__(self, c_input, v_input, w_input):
        self.__capacity = 0
        self.__values = []
        self.__weights = []

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

    def capacity(self):
        return self.__capacity

    def values(self):
        return self.__values

    def weights(self):
        return self.__weights

    def items(self):
        items = list()
        for i in range(len(self.__values)):
            items.append((self.__values[i], self.__weights[i]))
        return items
