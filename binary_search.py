import sys

def binary_search(a, x):
    low = 0
    high = len(a)-1
    middle = 0
    while low <= high:
        middle = (low+high)//2
        if x == a[middle]:
            return middle
        elif x > a[middle]:
            low = middle + 1
        elif x < a[middle]:
            high = middle - 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')