# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:39:58 2016

@author: inouek
"""

"""
練習問題 その1
0 から 100 までの整数がランダムに格納されたリストを返す関数 randlist を作成してください。
引数でリストのサイズを指定します。
"""

class RandList:
    
    #randomモジュールをインポート
    import random
    # リスト数値を格納する    
    def mkdir_list(input):
        list = []
        for count in input:
            # 0から100の数値をランダムで格納
            data = random.randomint(0, 100)
            list.append(data)
        
        # ランダムに格納されたリストの中身を表示する
        print list

if __name__ == '__main__':
    
     # コマンド上から数値を入力する。
    input = raw_input("整数値を入力してください")
    RandList.mkdir_list(input)
    
    
    
    
        