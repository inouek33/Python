# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:52:29 2016

@author: inouek
"""
"""
与えられた数までの素数を列挙する
処理にかかった時間を計測しておくと、自分の技術向上に伴って処理時間が短くなっていくのがよくわかる
"""

class Practice03_01:
    try:
        # コマンドラインから値を入力させる
        input = int(raw_input("整数を入力してください--->"))
        
        # 入力された値までの素数を格納するリストを用意
        #list = []
        
        #count = 1
        
        # 入力された値までループさせて素数判断を行う
        """
        for x in range(input):
            result = 0
            print x
            result_kari = x + 1
            
            for y in range(result_kari):
                print y
                y = y + 1
                if result_kari % y == 0 and y != 1:
                    result = result + 1
                
                if result == 1:
                    list.append(result_kari)            

        print list
        """
        # 2が素数なのは確定しているので、先に格納しておく
        list = [2]
        
        # 2から入力された値までのループ処理
        for i in range(2, input + 1):
            # listまでのループ処理
            for h in list:  # リストのなので、range()をつける必要はない
                if i % h == 0:
                    break;
                
                else:
                    if max(list) == h:
                        list.append(i)
                        
        print list
                        
                    
    except ValueError:
        print "入力された値は整数ではありません。"
        