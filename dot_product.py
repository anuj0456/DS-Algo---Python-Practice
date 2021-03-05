import sys

def cal_revenue(profits, clicks):
    rev = 0
    used = []
    profits.sort(reverse=True)
    clicks.sort(reverse=True)
    for i in profits:
        temp = 0
        z = -1
        for x, j in enumerate(clicks):
            if i*j > temp and x not in used:
                temp = i*j
                z = x
        used.append(z)
        rev += temp
    return rev

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    profits = data[1:n+1]
    clicks = data[1+n:len(data)]
    print(cal_revenue(profits, clicks))