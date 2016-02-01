# Python : if文の勉強
#
# コマンドプロンプト上から整数値を入力させる。
x = int(raw_input("Please enter an integer: "))

# 条件分岐に応じて、出力内容を変更する。
if x < 0:
    x = 0
    print "Negative changed to zero"
elif x == 0:
    print "Zero"
elif x == 1:
    print "Single"
else:
    print "More"
