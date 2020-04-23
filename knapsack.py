class Knapsack:
    """Class to hold knapsack related data. Namely Capacity, available items, and the weights for those items
    capacity is a single number value. values and weights are lists of numbers."""
    def __init__(self):
        self.capacity = 0
        self.weights = []
        self.values = []

    def get_data(self, c_input, v_input, w_input):
        print("capacity input filename:", c_input)
        print("values input filename:", v_input)
        print("weights input filename:", w_input)

        with open(c_input) as c_file:
            c_data = c_file.read()

        with open(v_input) as v_file:
            v_data = v_file.read()

        with open(w_input) as w_file:
            w_data = w_file.read()

        print(c_data)
        print(v_data)
        print(w_data)




