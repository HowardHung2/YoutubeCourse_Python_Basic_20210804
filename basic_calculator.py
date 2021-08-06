# 建立一個基本計算機
from typing import AsyncGenerator


name = input("請輸入您的名字 : ")
print("哈囉, " + name + "\n歡迎體驗簡易計算機")
print("＝＝＝＝第一部分 整數計算機＝＝＝＝")
num1 = input("請輸入第一個整數數字 :")
num2 = input("請輸入第二個整數數字 : ")
print(int(num1)+int(num2))

print("＝＝＝＝第二部分 小數計算機＝＝＝＝")
num3 = input("請輸入第一個小數數字 :")
num4 = input("請輸入第二個小數數字 : ")
print(float(num3)+float(num4))
