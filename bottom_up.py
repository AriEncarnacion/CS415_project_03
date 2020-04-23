class BottomUp:
    def __init__(self, items, capacity):
        self.__items = items
        self.__n = len(items)
        self.__W = capacity
        self.__table = [[0 for col in range(self.__W + 1)] for row in range(self.__n + 1)]

    def optimal_value(self):
        self.__fill_table()
        return self.__table[self.__n][self.__W]

    def __fill_table(self):
        for row in range(self.__n + 1):
            for col in range(self.__W + 1):
                self.__table[row][col] = self.__F(row, col)

    def __F(self, i, j):
        if i > 0 and j > 0:
            v = self.__items[i-1][0]
            w = self.__items[i-1][1]
        else:
            v, w = 0, 0

        if i == 0:
            return 0

        if j == 0:
            return 0

        if j - w >= 0:
            return max(self.__F(i - 1, j), v + self.__F(i - 1, j - w))

        return self.__F(i - 1, j)

    def optimal_subset(self):
        print("f")

    def debug_print_table(self):
        for row in self.__table:
            print(row)
        print("---------")


