# ループ内部でイテレートしているシーケンスを修正する際のスライス
words = ["cat", "window", "defenestrate"]

for w in words[:]:
# 上記の一文を "for w in words:" にしてしまうと永久ループとなるのは何故か？
# insert と 出力による違いなのか？ 要確認項目。
    if len(w) > 6:
        words.insert(0, w)
