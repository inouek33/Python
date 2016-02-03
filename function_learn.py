# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:02:25 2016

@author: inouek
"""

# 関数の定義方法をもう少し検証する
def ask_ok(prompt, retries = 4, complaint = 'Yes or No, please'):
    while True:
        
        input = raw_input(prompt)
        if input in ('y', 'ye', 'yes'):
            return True
        
        if input in ('n', 'no', 'nop', 'nope'):
            return False
            
        retries = retries - 1
        
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

# 必須の引数のみを関数に渡す場合
ask_ok('Do you really want to quiet?')

# 1つのオプション引数を渡す場合
ask_ok('OK to overwrite the file?', 2)

# 全ての引数を渡す場合
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')