def cal_fibonacci_huge(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    z = []
    for i in range(n - 1):
        z.append(previous)
        previous, current = current, (previous + current)%m
        print(i, previous, current)
        if n > 1600 and previous == 0 and current == 1:
            cycle = i+1
            x = n % cycle
            return z[x]
    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(cal_fibonacci_huge(n, m))

