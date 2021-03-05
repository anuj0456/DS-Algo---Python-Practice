# Uses python3
import sys

def cal_gcd(a, b):
    current_gcd = a
    temp = b
    while temp > 0:
        current_gcd, temp = temp, current_gcd%temp
    return current_gcd

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(cal_gcd(a, b))
