
def cal_change(n):
    count = 0
    while n > 0:
        if n >= 10:
            n = n - 10
        elif 10 > n >= 5:
            n = n - 5
        else:
            n = n - 1
        count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    print(cal_change(n))