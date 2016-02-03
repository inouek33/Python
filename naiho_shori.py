# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:41:30 2016

@author: inouek
"""

# リストを内包してみる
# 1から10までの値を2乗してリストに表示する処理
data = []

for x in range(10):
    data.append(x ** 2)

print data
print

# 上記の処理を１つにまとめる
input = [x ** 2 for x in range(10)]
print

# 2重のループ処理でもかつ条件がある場合の関数
combination = []
for a in [1, 2, 3, 4, 5]:
    for b in [5, 4, 3, 2, 1]:
        if a == b:
            combination.append((a,b))

print combination

# これを1文にまとめてみた
data = [(x, y) for x in [1, 2, 3, 4, 5] for y in [5, 4, 3, 2, 1] if x == y]
print


matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

print [[row[i] for row in matrix] for i in range(4)]
print


# 上記の１文は以下と道義となる
data_list = []
for i in range(4):
    data_list.append([row[i] for row in matrix])

print data_list
print


# さらに分割
list = []
for i in range(4):
    data = []
    
    for row in matrix:
        data.append(row[i])
    
    list.append(data)

print list
print
    




    
