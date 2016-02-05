# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:26:00 2016

@author: inouek
"""

"""
<ループ処理の問題>
Hello World![改行]を5回表示させてください。 
print(或いはprintf,cout等)を5回コピーすれば当然可能ですが、
ループ構文(for,while等)を利用して、print等は1回の使用にとどめてみてください。

可能ならコマンドラインから入力を受け取って、n回表示するように改造してください。
何回目のHello World!かも表示してみてください。
"""

class Practice01:
    # コマンドラインから何回表示させるか入力させる。
    try:
        # 数値の入力を促し、コマンドラインから入力させる処理
        print "何回出力させますか？"
        input = int(raw_input("整数値を入力してください--->"))

        i = 0
        # 入力された数値の回数分、出力のループ処理を行う        
        while i < input:
            print "Hello World !"
            
            i = i + 1
    
    except ValueError:
        print "入力内容が整数ではありません"
        
        