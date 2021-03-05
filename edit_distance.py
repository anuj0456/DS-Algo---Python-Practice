def cal_distance(a, b):
    m = len(a)+1
    n = len(b)+1
    D = {}
    for j in range(1,n):
        for i in range(1,m):
            insert = dist(D, i, j-1) + 1
            delete = dist(D, i-1, j) + 1
            match = dist(D, i-1, j-1)
            mismatch = dist(D, i-1, j-1) + 1
            x = getKey(j, i)
            if a[i-1] == b[j-1]:
                D[x] = min(insert, delete, match)
            else:
                D[x] = min(insert, delete, mismatch)
    return dist(D, m-1, n-1)

def dist(D, i, j):
    if j == 0 and i > 0:
        return i
    elif i == 0 and j > 0:
        return j
    elif i < 0 or j < 0:
        return 0
    elif i == 0 and j == 0:
        return 0
    else:
        x = getKey(j, i)
        return D[x]

def getKey(i,j):
    return str(i)+str(j)


if __name__ == "__main__":
    a = input()
    b = input()
    print(cal_distance(a, b))