import sys

def get_max_weight(W, a):
    val_w_i = [[0]*(W+1) for _ in range(len(a)+1)]
    v = a
    n = len(a)
    for w in range(1, n+1):
        for i in range(1, W+1):
            val_w_i[w][i] = val_w_i[w-1][i]
            if a[w-1] <= i:
                val = val_w_i[w-1][i-a[w-1]]+v[w-1]
                if val_w_i[w][i] < val:
                    val_w_i[w][i] = val
    return val_w_i[n][W]

if __name__ == "__main__":
    W, n, *a = map(int, sys.stdin.read().split())
    print(get_max_weight(W, a))
