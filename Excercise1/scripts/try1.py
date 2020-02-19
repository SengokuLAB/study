# -*- coding:utf-8 -*-

# 編集したいファイル（元ファイル）を開く
file = open("13101.csv","r",encoding = "utf_8")

# 書き出し用のファイルを開く
out_file = open("13101_edit.csv","w")

# 書き出し用ファイルのヘッダーを記述.
out_file.write("形状ID,町丁目,面積\n")

# 元ファイルのヘッダーをreadlineメソッドで１行飛ばす(1行だけ読む)
file.readline()

# 元ファイルのレコード部分をreadlinesメソッドで全行を読み取る
lines = file.readlines()

# for文で1行ずつ取得
for line in lines:

    # 改行コードをブランクに置換
    line = line.replace("\n","")

    # カンマ区切りでリストに変換する
    line = line.split(",")

    # 変換後のカンマ区切りの雛形を作り、変換処理した値を入れ込む
    row = "{},{},{}\n".format(
        line[0],
        line[3]+ line[5]+ line[6]+ line[7],
        line[25] #ここを line[25].replace("A","B") とかするとカラムのAをBに変換可
        )

    # 書き出し用のファイルに出力
    out_file.write(row)

# ２つのファイルを閉じる
file.close()
out_file.close()
