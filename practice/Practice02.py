# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:48:29 2016

@author: inouek
"""
"""
なんか偉い人が考えた問題
ルールは以下の通り
1から順番に数を表示する
その数が3で割り切れるなら"Fizz"、5で割り切れるなら"Buzz"、両方で割り切れるなら"FizzBuzz"と表示する
要するに"1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz ･･･"と出力される
プログラマかどうかがわかるんだとさ
実行例
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz ・・・
"""

class Practice02:    
    # 数値を格納する変数を宣言
    data = ["Fizz", "Buzz"]
    count = 1
    
    for i in range(100):
        if count % 3 == 0 and count % 5 == 0:
            print data[0] + data[1],
        
        elif count % 3 == 0:
            print data[0],
            
        elif count % 5 == 0:
            print data[1],
            
        else:
            print count,
        
        count = count + 1
        
            
    
    