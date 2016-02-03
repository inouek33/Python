# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:47:13 2016

@author: inouek
"""

# raw_input()について不明点があるので学習
# 名前入力を促し、名前コマンド上から入力させる
name = raw_input("Enter the your name!")
#　入力された名前を出力する。
print name


# スコープ関しての扱い
# 関数が定義された時点で、関数を定義している側のスコープが評価される。
i = 6

def output(args = i):
    print args

i = 5
output()

i = 7
output(7)

# デフォルトの評価は一度しか行わない扱いの調査
def f(a, L = []):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

# 上記の方法を解除するための回避方法
def f2(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L
    
print f2(1)
print f2(2)
print f2(3)