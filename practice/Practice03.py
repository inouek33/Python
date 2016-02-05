# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:04:36 2016

@author: inouek
"""
"""
与えられた数が素数かどうか調べる
あるいは与えられた数までの素数を列挙する
処理にかかった時間を計測しておくと、自分の技術向上に伴って処理時間が短くなっていくのがよくわかる
"""

class Practice03:
    try:
        # 数値を１入力させる
        input = int(raw_input("整数を1つ入力してください--->"))
        # 入力された値を別の変数に格納させる
        data = input
        
        count = 1
        result = 0
        
        # ループで素数か判断させる
        for i in range(input):
            
            # 1とそれ自身の数でしかわれない値が素数なのため、
            # 1は判定フラグでチェックする
            if input == 1:
                print str(input) + "は素数ではありません"
                break;
            
            # 入力された値が割り切れるか確認
            if input % count == 0:
                result = result + 1
            
            # 素数か判定する
            # resultが2以外のものは素数ではないと判断する
            if result > 2:
                print result
                print str(input) + "は素数ではありません"
                break;
            
            count = count + 1
            
        if result == 2:
            print str(input) + "は素数です"
        
        
    except ValueError:
        print "整数を1つ入力してください !"