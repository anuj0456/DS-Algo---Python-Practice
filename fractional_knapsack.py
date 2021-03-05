import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    while capacity > 0:
        if len(values) == 0:
            return value
        unit = -1
        index = -1
        for i in range(len(values)):
            if values[i] != 0 and weights[i] != 0 and float(values[i]/weights[i]) > unit:
                unit = float(values[i]/weights[i])
                index = i
        if index != -1:
            if capacity >= weights[index]:
                value += values[index]
                capacity -= weights[index]
            elif capacity < weights[index]:
                value += float(values[index]*capacity/weights[index])
                capacity -= capacity
        weights.pop(index)
        values.pop(index)
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))