# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:42:10 2016

@author: inouek
"""

"""
2つのファイルを並列に表示するプログラム

"""

class ReadWrite:
    # テキストを開く
    f = open("/Users/inouek/Desktop/Python/import/bytecode.txt")
    
    # 値を保持する配列を宣言
    outfile = []
        
    # テキストを1行ずつ読み込む
    line = f.readline()
    
    for input in f:
        outfile.append(input)
    
    print outfile
