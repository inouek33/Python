# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:35:49 2016

@author: inouek
"""

# リストを利用したstack と queue
# stackの扱い
# 空のリストを作成する
stack = []

# 空のリストであることを確認する
print stack

# リストに中身を投入する
stack = range(1,11)

# 中身を再度確認する
print stack

# リストに中身を追加
stack.append(11)
stack.append(12)
stack.append(13)

# 中身を再度確認する
print stack

# リストの中身を取り出す
stack.pop()
stack.pop()
stack.pop()

# 中身を再度確認する
print stack

print
print


# queueの扱い
# collections.deque を使用する
from collections import deque
data = deque([0, 1, 2, 3, 4, 5])
data.popleft()
data.popleft()
data.popleft()

print data
