import sys


def partition3(a, l, r):
    x = a[l]
    j = l
    k = r
    i = j
    #
    while i <= k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
        elif a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
            i -= 1
        i += 1
    return j, k


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    p1, p2 = partition3(a, l, r)
    randomized_quick_sort(a, l, p1 - 1)
    randomized_quick_sort(a, p2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
