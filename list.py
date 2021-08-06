# 列表 list 及 列表用法
scores = [90,70,60,50,80]
friends = ["秉榮","小榮","阿榮"]
information = ["秉榮",170,17]
print("名字 : " + information[0])
print("年紀 : " + str(information[-1])) # -1為倒數第x位
print("身高 : " + str(information[-2])) # -2為倒數第x位
print("== 前兩次成績 ==")
print(scores[0:2]) #從第0位開始取到第二位(不含)
print("== 所有成績(除第一次) ==")
print(scores[1:]) #從第1位開始取到最後一位
print("== 所有成績(除最後一次) ==")
print(scores[:4]) #從第4位以前取到第一位

print("== 列表末加上值 ==")
scores.append(30) # 列表末加上值
print(scores)

print("== 列表第幾位插入值 ==")
scores.insert(2,100) # (第幾位, 插入值) 列表第幾位插入值
print(scores)

print("== 刪除列表中所以的某值 ==")
scores.remove(90) # 刪除列表中所以的某值
print(scores)

print("== 刪除列表的最後一位 ==")
scores.pop # 刪除列表的最後一位
print(scores)

print("== 由小到大排列 ==")
scores.sort() # 由小到大排列
print(scores)

print("== 列表的數值反轉 ==")
scores.reverse() # 列表的數值反轉
print(scores)

print("== 尋找某值的位置 ==")
print(scores.index(50)) # 尋找某值的位置

print("== 計算有幾個某數值 ==")
print(scores.count(50)) # 計算有幾個某數值

print("== 結合列表 ==")
scores.extend(friends) # 結合列表
print(scores)

print("== 長度列表 ==")
print(len(scores)) #長度

print("== 清除列表的所有值 ==")
scores.clear() # 清除列表的所有值
print(scores)

