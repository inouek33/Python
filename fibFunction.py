# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:01:55 2016

@author: inouek
"""

# フィボナッチ数列を使用した関数を定義
def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a,b = b, a+b

# 上記で記述した関数呼び出し、結果をコンソールに表示
fib(2000)
# 改行の手段として、printを記述
print

# 変数に関数を代入して、変数で関数を実行
function = fib
function(10)
# 改行の手段として、printを記述
print

#　引数がない場合に関数が何の値を返り値として返すかの確認
print function(0)


# リストを表示するのではなく、値を返す関数に変更
def fibonacci(m):
    # リストを定義
    result = []
    
    x, y = 0, 1
    while x < m:
        # リストの末尾に値を追加をしていく
        result.append(x)
        x, y = y, x+y
        
    return result

# 動作検証
data = fibonacci(50)
print data   