# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:35:46 2016

@author: inouek
"""
"""
入力した数値を制限値として、
配列にランダムな数値を格納して表示するプログラム
"""

import random

class RandomList:
    
    # ランダムな値を格納する関数
    def ramdomList(data):
        list = []
        for i in range(data):
            list.append(random.randint(0, 100))
        print list
        
    # 入力されたかどうかを判定する関数
    def isEmptyString(input):
        if len(input) == 0:
            judge = False
        else:
            judge = True
        
        return judge
    
    
    # メイン関数
    if __name__ == '__main__':
        flag = False
        print flag
        input = raw_input("整数値を入力--->")
        
        try:
            check = isEmptyString(input)
            print input
        
            if check == False:
                input = "10"
            
            limit = int(input)
        
            ramdomList(limit)
        
        # 入力値が数値以外の場合は例外処理
        except ValueError:
            print "入力された値が数値ではありません。"