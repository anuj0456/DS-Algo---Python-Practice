def get_min_change(m, c):
    total = 0
    numOfCoins = [0]*(m+1)
    if m < 0:
        return 0
    elif m == min(c):
        numOfCoins[m] = 1
    else:
        while total < m:
            total += 1
            for i in c:
                if total >= i:
                    count = numOfCoins[total-i] + 1
                    if numOfCoins[total] == 0:
                        numOfCoins[total] = count
                    elif count < numOfCoins[total]:
                        numOfCoins[total] = count
    return numOfCoins[m]

if __name__ == "__main__":
    money = int(input())
    coins = [1, 3, 4]
    print(get_min_change(money, coins))