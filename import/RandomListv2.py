# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:06:30 2016

@author: inouek
"""

"""
制限値以外にも、ランダムに値を取得する数値を変数値と入力できるようにしたプログラム
何も入力せずにEnterされた時の対応が必要っぽい
"""

import random

class RandomListv2:
    
    # ランダムなリストを取得する関数
    def getList(size, lower=0, upper=100):
        
        # 値格納用リストを宣言
        list = []
        
        # 制限値を元にイテレート処理
        for x in range(size):
            list.append(random.randint(lower, upper))
        
        # 結果を表示
        print list


    # メイン関数
    if __name__ == '__main__':
        
        """
        # サイズを入力10
        input_size = int(raw_input("何個の数値を表示させるか？--->"))
        input_lower = int(raw_input("ランダムに取得する数値の下限は？--->"))    
        input_upper = int(raw_input("ランダムに取得する数値の上限は？--->"))
        
        #　関数に渡す
        getList(input_size, input_lower, input_upper)
        """
        
        getList(10)
        getList(5, 90)
        getList(15, 80, 100)