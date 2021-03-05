
def cal_lcm(a, b):
    current_gcd = a
    temp = b
    while temp > 0:
        current_gcd, temp = temp, current_gcd % temp
    return int(a*b/current_gcd)


if __name__ == "__main__":
    a, b = map(int, input().split())
    if a > b:
        print(cal_lcm(a, b))
    else:
        print(cal_lcm(b, a))



