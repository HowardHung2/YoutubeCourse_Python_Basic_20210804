# 元組 tuple 避免被意外修改
scores = (90,60,89,55,67)
print(scores[0])
print(scores[0:2])

print(len(scores)) #長度

scores[0] = 30
print(scores)