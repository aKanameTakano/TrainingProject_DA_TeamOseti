#!/usr/bin/python
# -*- Coding: utf-8 -*-
import CsvAnalyze

# データ取得のサンプル
data = CsvAnalyze.AllBooks("comments")
# print(data["opus"])

myTitle = []
for i in data["opus"]:
  myTitle.append(i)
  # print(i)
# print("-----------------------------")

myTitle = list(set(myTitle))

print(len(myTitle))

print("=======================")
for title in myTitle:
  print(title)


# ソートのサンプル
# res1 = CsvAnalyze.CsvSort(data, "opus", True)
# print(res1)
# print("=========")


#特定行が欲しいサンプル　タイトルとコメントが出る
# res2 = CsvAnalyze.CsvExtraction(data, ["opus", "comments"])
# print(res2)


#全ファイルと欲しいタイトルを渡すとコメントが一気にもらえるもの
# res3 = CsvAnalyze.OutCommnet(data, "黒子のバスケ Replace PLUS")

# print("黒子のバスケ Replace PLUS")
# for i in CsvAnalyze.OutCommnet(data, "黒子のバスケ Replace PLUS"):
#   print(i)

# print("-------------------------")

# print("PSYREN―サイレン―")
# for i in CsvAnalyze.OutCommnet(data, "PSYREN―サイレン―"):
#   print(i)