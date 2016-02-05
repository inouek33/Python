# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:41:22 2016

@author: inouek
"""
"""
これはｎ桁の数を探すゲームです。適当な数を入れると桁も数字もあっていれば「Hit」としその個数が、数字はあっているが桁が異なっていれば「Blow」としてその個数が出力されます。それを繰り返すことで答えを探すことができます。このゲームを作成しなさい。答えの数は乱数を使って毎回別の答えを用意しましょう。
具体的には
正解が1234だとして
4321　と入力　4blow
1245　と入力　2hit　1blow
なおルール上4422などのゾロ目の正解は出ないようにしましょう。
"""

import random

class HitAndBlow:
    # 答えを可能する変数を用意しておく
    final_answer = []
    # プレイヤーに桁数を決めてもらう
    print "ゲームを開始するにあたり、桁数を決めます"
    input_ketasu = raw_input("桁数を入力してください---->")
    
    # 数字か文字列かを判断する処理    
    check_int = input_ketasu.isdigit()
    
    while check_int == False:
        print "入力された値は数字ではありません"
        input_ketasu = raw_input("「整数値」を入力し、桁数を決定してください---->")
        
        check_int = input_ketasu.isdigit()
    
    ketasu = int(input_ketasu)
    print input_ketasu + "桁でゲームを開始いたします"
    
    for x in range(ketasu):
        if x == 0:
            data = random.randint(1, 9)
            final_answer.append(data)
        
        else:
            data = random.randint(1, 9)
            while final_answer[x-1] == data:
                data == random.randint(1, 9)
            
            final_answer.append(data)
    
    print final_answer
        
        
        
    
