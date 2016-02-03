# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:17:47 2016

@author: inouek
"""

# filter, map, reduce の取り扱い
# 1から30までの数の中で、3と5で割り切れる値を返す関数
def keisan(x): return x % 3 == 0 or x % 5 == 0
    
print filter(keisan, range(1, 31))
print

#️1から10の間で、3乗された値を返す関数
def cube(y): return y * y * y

print map(cube, range(1, 11))
print


# 仮引数が複数のものにも対応が可能
seq = range(8)
print seq
def square(a, b): return a + b

print map(square, seq, seq)
print


# 上記で作成した関数を用いて、reduceメソッドを使用してみる
# 1から10までの値の総和を求める
print reduce(square, range(1, 11))
print


# 関数の中に関数を作成する
def kansu(x):
    def suji_add(a, b): return a + b
    
    return reduce(suji_add, x, 0)

print kansu(range(1, 11))
print kansu([])