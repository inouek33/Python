# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:32:42 2016

@author: inouek
"""
"""
入力された整数がグレゴリオ暦（いつも使ってるやつ）でうるう年であるか判定せよ
西暦が4で割り切れる年はうるう年
ただし、4で割り切れても100で割り切れる年はうるう年でない
ただし、100で割り切れても400で割り切れる年はうるう年
"""
class LeapYear:
    try:
        # 西暦を入力
        input = int(raw_input("西暦を入力してください!(数字4桁---->"))

        # 4で割り切れるかどうかの確認        
        if input % 4 == 0:
            # 100で割り切れるかどうかの確認
            if input % 100 == 0:
                # 400 で割り切れるかどうかの確認
                if input % 400 == 0:
                    print "西暦" + str(input) + "年は閏年です。"
                else:
                    print "西暦" + str(input) + "年は閏年ではありません。"
                    
            else:
                print "西暦" + str(input) + "年は閏年です。"
            
        else:
            print "西暦" + str(input) + "年は閏年ではありません。"
            
    
    except ValueError:
        print "入力された値が数字ではありません"
  
    
    