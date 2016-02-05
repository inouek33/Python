# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:37:38 2016

@author: inouek
"""
"""
これは答えの数を探すゲームです。適当な数を入れると正解よりも大きいか小さいか,または正解であるか出力されます。
それを繰り返すことで答えを探すことができます。このゲームを作成しなさい。答えの数は乱数を使って毎回別の答えを用意しましょう。
"""

import random

class KazuateGame:
    
    # 答えとなる数字を乱数で取得
    # 0 〜 1000までの値とする
    final_answer = random.randint(1, 1000)
    
    print "---- Game Start ----"
    
    # 数字を入力させる処理(関数)
    def input_check():
        # 数字を入力させる処理
        input = raw_input("数字を入力してください--->")
        # 入力された値が数字かどうか判断する処理
        check = input.isdigit()
        # 数字でなけれな、数字が入力されるまでループさせる処理
        while check == False:
            print "入力された値は数字ではありません"
            input = raw_input("もう一度、数字を入力してください--->")
        
            check = input.isdigit()
        
        # 値を返却する
        int_input = int(input)
        return int_input
        
    # 入力文字列をInt型に変換
    answer = input_check()
    
    #print answer
    #print int(answer)
    
    # 処理開始
    while answer != final_answer:
        if answer < final_answer:
            print "正解はもっと大きい数字です"
        elif answer > final_answer:
            print "正解はもっと小さい数字です"
        else:
            break
        
        answer = input_check()
    
    print "正解です!"    