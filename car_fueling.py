import sys

def compute_min_refills(d, m, stops):
    count = 0
    left_over = stops
    while d > 0:
        if d < m:
            return -1
        if len(left_over) == 0:
            return count
        for i in range(len(left_over)):
            if i+1 < len(left_over) and m > left_over[i+1]:
                continue
            else:
                left_over = left_over[i+1:]
                count += 1
                d -= stops[i]
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))