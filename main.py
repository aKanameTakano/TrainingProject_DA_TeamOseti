#!/usr/bin/python
# -*- Coding: utf-8 -*-
import CsvAnalyze
import MeCab

# データ取得のサンプル
data = CsvAnalyze.AllBooks("comments")
# print(data["opus"])
# print("=======")

# ソートのサンプル
# res1 = CsvAnalyze.CsvSort(data, "opus", True)
# print(res1)
# print("=========")


#特定行が欲しいサンプル　タイトルとコメントが出る
# res2 = CsvAnalyze.CsvExtraction(data, ["opus", "comments"])
# print(res2)


#全ファイルと欲しいタイトルを渡すとコメントが一気にもらえるもの
res3 = CsvAnalyze.OutCommnet(data, "黒子のバスケ Replace PLUS")

print("黒子のバスケ Replace PLUS")
for tes in res3:
  print(tes)