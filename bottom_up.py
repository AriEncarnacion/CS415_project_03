
def F(values, weights, W):
    n = len(values)  # item count
    table = [[-1 for col in range(W + 1)] for row in range(n + 1)]

    for row in table:
        print(row)
    print("---------")
