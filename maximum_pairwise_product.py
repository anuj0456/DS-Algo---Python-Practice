# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:53:34 2020

@author: Anuj.Gupta
"""


def highest_two_num(lst):
    a = lst[0]
    b = lst[1]
    index_a = -1
    if len(lst) > 2:
        for i in range(len(lst)):
            if lst[i] > a:
                a = lst[i]
                index_a = i
        for i in range(len(lst)):
            if i != index_a and  lst[i] > b:
                b = lst[i]      
    return a*b


if __name__ == "__main__":
    n = int(input())
    z = [int(x) for x in input().split()]
    print(highest_two_num(z))