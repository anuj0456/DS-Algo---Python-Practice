import sys

def can_partition(num):
    s = sum(num)
    if s % 3 != 0:
        return 0

    s = int(s / 3)

    n = len(num)
    dp = [[0 for x in range(s+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 1

    for j in range(1, s+1):
        if num[0] == j:
            dp[0][j] = 1
        else:
            dp[0][j] = 0

    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    return dp[n - 1][s]


if __name__ == "__main__":
    n, *a = map(int, sys.stdin.read().split())
    print(can_partition(a))
    # n = random.randrange(1, 100)
    # a = []
    # test = 0
    # check = True
    # while check:
    #     for i in range(n):
    #         a.append(random.randrange(0, 100))
    #     print(a)
    #     print(partition(a))
    #     if len(a) == 0:
    #         check = False
    #     # test += 1