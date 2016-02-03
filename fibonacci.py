# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:42:24 2016

@author: inouek
"""

# Fibonacci number module
# 関数その1
def fib1(n):
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a+b


# 関数その2
def fib2(m):
    data = []
    a, b = 0, 1
    while b < m:
        data.append(b)
        a, b = b, a+b
    
    return data