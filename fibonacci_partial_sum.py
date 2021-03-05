def get_partial_sum(m, n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    z = []
    x = -1
    for _ in range(n + 1):
        z.append(previous)
        previous, current = current, (previous + current)%10
        if previous == 0 and current == 1:
            if m > len(z):
                x = m%len(z)
            else:
                x = m
            y = n % len(z)
            return (sum(z)-sum(z[:x])+sum(z[: y+1]))%10
    return sum(z[m:n+1])%10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(get_partial_sum(m, n))