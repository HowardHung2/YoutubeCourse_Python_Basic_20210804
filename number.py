#如何使用數字、數字的用法

from math import *

print(8/5) # 輸出 1.6

print(8//5) # 輸出 1 //為整數除法

print(8+8*5) # 輸出 48 具有先乘除後加減(含先刮號的先算)

num = 8
print(num * 5) 
print(num % 5) # %為取餘數

print("會印出數字" + str(num)) # 數字轉字串
#print( 8 + str(num)) # 無法將字串及數字相加，否則出現錯誤

print(abs(-123)) # 取絕對值

print(pow(2, 4)) # 次方運算

print(max(2, 3, 4, 5, 6, 100)) # 回傳最大值
print(min(2, 3, 4, 5, 6, 100)) # 回傳最小值

print(round(4.6)) # 四捨五入
print(round(4.4)) # 四捨五入

print(floor(4.4)) # 無條件捨去
print(floor(5.1)) # 無條件捨去

print(ceil(7.8)) # 無條件進位
print(ceil(8.2)) # 無條件進位

print(sqrt(64)) # 開根號
print(sqrt(36)) # 開根號