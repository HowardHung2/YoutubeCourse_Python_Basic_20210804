#如何使用字串、字串的用法

print("Hello, Howard")

print("Hello\"Howard") # 將 " 作為字串的一部分，可在前輸入 \

print("Hello" + "Howard")

print("Hello" + ", Howard")

wel = "Welcome"
name = "howard"
print(wel.lower() + ", " + name.upper()) # .lower()將字串轉為小寫 .upper()將字串轉為大寫
print(wel.isupper())  # .isupper() 判斷字串是否都為大寫
print(name.islower()) # .islower() 判斷字串是否都為小寫

wel = "Welcome"
print(wel[0]) #[ ]內可輸入數字來指定字串位置

wel = "Welcome"
print(wel.index("o"))  # .index("o") 尋找字串中該字的位置

wel = "Welcome"
print(wel.replace("W","w"))  # .replace(" "," ") 尋找字串中該字後取代為後者