# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:26:14 2016

@author: inouek
"""

# キーワード引数の扱いに関して
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print "-- This parrot would't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    
# 上記の関数を呼び出す
parrot(1000)
print
parrot(voltage=100)
print
parrot(voltage=100000, action="VOOOOOOOOM")
print
parrot(action="VOOOOOOOOM", voltage=100000)
print
parrot("a milion", "bereft of life", "jump")
print
parrot("a thousand", state="pushing up the daisies")
print
print


# 応用編
def cheeseshop (kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
        
# 呼び出し方法
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")
print
print
           

# 引数リストのアンパック
print range(3, 6)
args = [3, 6]
print range(*args)
print
print


# lambda式 その1
def increment(n):
    return lambda x: x+n

f = increment(42)
print f(1)
print
print

# lambda式 その2
data = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
data.sort(key = lambda data: data[1])
print data

