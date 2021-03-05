# Uses python3
def calc_fib(n):
    x = [0, 1]
    if n > 1:
        for i in range(2, n+1):
            x.append(x[i-1] + x[i-2])
    print(x)
    return x[n]

n = int(input())
print(calc_fib(n))
