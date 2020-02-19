# -*- coding:utf-8 -*-

import csv
import pandas as pd

# 編集したいファイル（元ファイル）を開く
file = open("13101.csv","r",encoding = "utf_8")

newcsv = []

top_list = ['形状ID','adress']

newcsv.append(top_list)


# for文で1行ずつ取得
for i in csv.DictReader(file):

    line = []
    line.append(i['\ufeff"形状ID"']) #dictreaderで開いてKEYを確認した.\ufeffは謎
    line.append(" ".join((i["都道府県"],i["市区町村"],i["大字"],i["字丁目"])))

    newcsv.append(line)

#保存形式設定
out_file = csv.writer(open("13101_edit2.csv", "w"), lineterminator='\n')

#保存内容指定
out_file.writerows(newcsv)

#二つのcsvをDF化する
df1 = pd.read_csv("13101.csv", encoding = "utf_8")
df2 = pd.read_csv("13101_edit2.csv")

df = pd.merge(df1, df2, how="inner", on="形状ID")

# CSV ファイル  として出力
df.to_csv("13101edit_2a.csv")

# 元ファイルを閉じる
file.close()
