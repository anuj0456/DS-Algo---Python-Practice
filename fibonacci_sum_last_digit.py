def get_fibonacci_last_digit_sum(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    z = []
    for _ in range(n + 1):
        z.append(previous)
        previous, current = current, (previous + current)%10
        if previous == 0 and current == 1:
            x = n%len(z)
            return (sum(z[: x+1])) % 10
    return sum(z)%10

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_sum(n))