import sys

# below solution was submitted first and it passed the test
def cal_maj_ele(a):
    x = 0
    dic = {}
    while x < len(a):
        if a[x] in dic:
            dic[a[x]] += 1
        else:
            dic[a[x]] = 1
        if dic[a[x]] > len(a)//2:
            return 1
        x += 1
    return 0

if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(cal_maj_ele(a))

# actual divide and conquer logic
# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#
#     return -1
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)