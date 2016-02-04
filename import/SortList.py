# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:32:24 2016

@author: inouek
"""

"""
比較関数を関数に渡してソートするプログラム
"""

"""
class SortList:
    # ソートを行う関数を定義
    def qsort(list):
        if list == []:  # 渡された変数(リスト)に値が何も入っていない場合
            return list
        else:           # それ以外の場合
            def partition(x, list):
                a, b = [], []
                
                for i in list:
                    if i < x:
                        a.append(i)
                    else:
                        b.append(i)
                
                return a, b
                
            xs, ys = partition(list[0], list[1:])
            return qsort(xs) + [list[0]] + qsort(ys)
                    
                

    # メイン関数
    if __name__ == '__main__':
        print qsort(list)
"""

"""
上記のようにクラスにする以下の1文がエラーとなる。
return qsort(xs) + [list[0]] + qsort(ys)
エラー内容は、qsortが定義されていないというもの。
理由がわからないので、調査したいところ。

"""

"""
def qsort(lst):
    if lst == []: # 仮引数に値がない場合
        return lst
        
    else:         # それ以外の場合
        def partition(x, lst):
            a, b = [], []
        
            for i in lst:
                if i < x:
                    a.append(i)
                else:
                    b.append(i)
                        
            return a, b
                
        xs, ys = partition(lst[0], lst[1:])
        return qsort(xs) + [lst[0]] + qsort(ys)
"""


def qsort(fn, lst):
  if lst == []:
    return lst
  else:
    def partition(x, lst):
      a, b = [], []
      for i in lst:
        if fn(i, x):
          a.append(i)
        else:
          b.append(i)
      return a, b
    xs, ys = partition(lst[0], lst[1:])
    return qsort(fn, xs) + [lst[0]] + qsort(fn, ys)


data = [2, 4, -90, 3, 10]
#print data[1:]
#print qsort(data)
print qsort(lambda x, y: x > y, [2, 4, -90, 3, 10])

x = lambda x, y: x > y, [2, 4, -90, 3, 10]
print x