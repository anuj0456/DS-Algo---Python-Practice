import sys

def optimal_sequence(n, a):
    x = n
    total = 0
    dict = {}
    sequence = []
    fcount = [0]*(n+1)
    if n <= 0:
        return 0
    elif n == 1:
        fcount[n] = 1
        sequence.append(1)
    else:
        while total < n:
            total += 1
            count = 0
            value = 0
            for i in a:
                if i == 1:
                    count = fcount[total-1]
                    value = total-1
                elif i == 2 and total%2 == 0 and fcount[total//2] < count:
                    count = fcount[total//2]
                    value = total//2
                elif i == 3 and total%3 == 0 and fcount[total//3] < count:
                    count = fcount[total//3]
                    value = total//3
            dict[total] = value
            fcount[total] = count + 1
        while x >= 1:
            sequence.append(x)
            x = dict[x]
    return fcount[n]-1, reversed(sequence)

input = sys.stdin.read()
n = int(input)
a = [1, 2, 3]
# print(optimal_sequence(n, a))
count, sequence = list(optimal_sequence(n, a))
print(count)
for x in sequence:
    print(x, end=' ')


# import sys
#
# def optimal_sequence(n, a):
#     total = 0
#     sequence = {k: [] for k in range(n+1)}
#     fcount = [0]*(n+1)
#     if n <= 0:
#         return 0
#     elif n == 1:
#         fcount[n] = 1
#     else:
#         while total < n:
#             total += 1
#             count = 0
#             for i in a:
#                 if i == 1:
#                     count = fcount[total-1]
#                 elif i == 2 and total%2 == 0 and fcount[total//2] < count:
#                     count = fcount[total//2]
#                 elif i == 3 and total%3 == 0 and fcount[total//3] < count:
#                     count = fcount[total//3]
#             fcount[total] = count + 1
#     return fcount[n]-1
#
# input = sys.stdin.read()
# n = int(input)
# a = [1, 2, 3]
# print(optimal_sequence(n, a))
# sequence = list(optimal_sequence(n, a))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')